import aiohttp

from job_crawler.board.board import Board
from job_crawler.job import Job


class Workday(Board):
	def __init__(self, company_name: str, company_logo_url: str) -> None:
		self.company_name = company_name
		self.company_logo_url = company_logo_url

	async def get_jobs(self, _session: aiohttp.ClientSession) -> list[Job]:
		return []
