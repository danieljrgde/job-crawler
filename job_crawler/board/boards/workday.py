"""Workday job board."""

import asyncio
import html
import logging
from datetime import datetime

import aiohttp

from job_crawler.board.board import Board
from job_crawler.job.job import Job, Location

logger = logging.getLogger(__name__)


class Workday(Board):
	"""Board backed by the Workday CXS job board API."""

	_BASE_URL = "https://{tenant}.{instance}.myworkdayjobs.com/wday/cxs/{tenant}/{site}"
	_PAGE_SIZE = 20  # maximum page size accepted by the CXS API

	def __init__(self, tenant: str, instance: str, site: str, company_name: str, company_logo_url: str) -> None:
		self.tenant = tenant
		self.instance = instance
		self.site = site
		self.company_name = company_name
		self.company_logo_url = company_logo_url
		self._base_url = self._BASE_URL.format(tenant=tenant, instance=instance, site=site)

	async def _fetch_page(self, session: aiohttp.ClientSession, offset: int) -> dict:
		payload = {"appliedFacets": {}, "limit": self._PAGE_SIZE, "offset": offset, "searchText": ""}
		async with session.post(f"{self._base_url}/jobs", json=payload) as response:
			response.raise_for_status()
			return await response.json()

	async def _fetch_external_paths(self, session: aiohttp.ClientSession) -> list[str]:
		"""Return the ``externalPath`` for every job posting."""
		# The API only reports ``total`` on the first page.
		first_page = await self._fetch_page(session, 0)
		total = first_page.get("total", 0)

		paths = [posting["externalPath"] for posting in first_page.get("jobPostings", []) if "externalPath" in posting]

		for offset in range(self._PAGE_SIZE, total, self._PAGE_SIZE):
			page = await self._fetch_page(session, offset)
			paths.extend(posting["externalPath"] for posting in page.get("jobPostings", []) if "externalPath" in posting)

		return paths

	async def _fetch_job(self, session: aiohttp.ClientSession, external_path: str) -> dict:
		async with session.get(f"{self._base_url}{external_path}") as response:
			response.raise_for_status()
			return await response.json()

	def _parse_job(self, data: dict) -> Job:
		"""Map a single Workday ``jobPostingInfo`` payload into a ``Job``."""
		info = data["jobPostingInfo"]
		start_date = info.get("startDate")
		country = (info.get("country") or {}).get("descriptor")
		return Job(
			id=info["id"],
			title=info["title"],
			description=html.unescape(info.get("jobDescription", "")),
			department=None,
			# Workday exposes the city as a bare string; ``postedOn`` is localized
			# relative text, so ``startDate`` is the only parseable posting date.
			location=[Location(country=country, state=None, city=info.get("location"))],
			date_posted=datetime.fromisoformat(start_date) if start_date else None,
			date_modified=None,
			contract_type=None,
			company_name=self.company_name,
			company_logo_url=self.company_logo_url,
			work_mode=None,
			link=info["externalUrl"],
		)

	async def get_jobs(self, session: aiohttp.ClientSession) -> list[Job]:
		"""Return the current list of job postings for this board."""
		try:
			external_paths = await self._fetch_external_paths(session)
		except aiohttp.ClientError as e:
			logger.warning("Workday fetch failed for tenant %s: %s", self.tenant, e)
			return []

		details = await asyncio.gather(
			*(self._fetch_job(session, path) for path in external_paths),
			return_exceptions=True,
		)
		jobs: list[Job] = []
		for path, detail in zip(external_paths, details, strict=True):
			if isinstance(detail, BaseException):
				logger.warning("Workday detail fetch failed for %s: %s", path, detail)
				continue
			try:
				jobs.append(self._parse_job(detail))
			except (KeyError, TypeError, ValueError):
				logger.exception("Failed to parse Workday job payload for %s.", path)
		return jobs
