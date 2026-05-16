import aiohttp

from job_crawler.board.board import Board
from job_crawler.job import Job


class Workday(Board):
    def __init__(self):
        pass

    async def get_jobs(self, _session: aiohttp.ClientSession) -> list[Job]:
        return []
