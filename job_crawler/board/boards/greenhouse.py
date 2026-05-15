"""Greenhouse job board."""

import html
import logging
from abc import abstractmethod
from datetime import datetime

import aiohttp
from job_crawler.board.board import Board
from job_crawler.job import Job

logger = logging.getLogger(__name__)


class GreenHouse(Board):
	"""Base class for boards backed by the Greenhouse job board API.

	Subclasses provide a ``board_token`` identifying the company's board;
	the rest of the fetching and error handling is shared. This class is
	intended to be mixed with ``Company``, which supplies ``name`` and
	``logo_url`` used when constructing ``Job`` instances.
	"""

	_BASE_URL = "https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs?content=true"

	# Provided by the ``Company`` mixin in concrete subclasses.
	name: str
	logo_url: str

	@property
	@abstractmethod
	def board_token(self) -> str:
		"""The Greenhouse board token for the company (e.g. ``"airbnb"``)."""
		...

	async def _fetch_jobs(self, session: aiohttp.ClientSession, url: str) -> dict:
		async with session.get(url) as response:
			response.raise_for_status()
			return await response.json()

	def _parse_job(self, data: dict) -> Job:
		"""Map a single Greenhouse ``jobs`` entry into a ``Job``."""
		first_published = data.get("first_published")
		updated_at = data.get("updated_at")
		return Job(
			id=str(data["id"]),
			title=data["title"],
			description=html.unescape(data.get("content", "")),
			department=None,
			location=[data["location"]["name"]],
			date_posted=datetime.fromisoformat(first_published) if first_published else None,
			date_modified=datetime.fromisoformat(updated_at) if updated_at else None,
			contract_type=None,
			company_name=self.name,
			company_logo_url=self.logo_url,
			work_mode=None,
			link=data["absolute_url"],
		)

	async def get_jobs(self, session: aiohttp.ClientSession) -> list[Job]:
		"""Return the current list of job postings for this board."""
		url = self._BASE_URL.format(board_token=self.board_token)
		try:
			data = await self._fetch_jobs(session, url)
		except aiohttp.ClientError as e:
			logger.warning("Greenhouse fetch failed for token %s: %s", self.board_token, e)
			return []

		jobs: list[Job] = []
		for raw in data.get("jobs", []):
			try:
				jobs.append(self._parse_job(raw))
			except (KeyError, TypeError, ValueError):
				logger.exception("Failed to parse Greenhouse job payload for token %s.", self.board_token)
		return jobs
