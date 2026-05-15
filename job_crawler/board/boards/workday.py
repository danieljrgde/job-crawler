import aiohttp
from job_crawler.board.board import Board
from job_crawler.job import Job


class Workday(Board):
	async def get_jobs(self, session: aiohttp.ClientSession) -> list[Job]:
		return []
