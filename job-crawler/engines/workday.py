from __future__ import annotations

import aiohttp
from engines.base import Engine, Job


class Workday(Engine):
	async def get_jobs(self, session: aiohttp.ClientSession) -> list[Job]:
		return []
