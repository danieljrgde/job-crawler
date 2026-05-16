import asyncio
import sys
from pathlib import Path

import aiohttp
import pytest

from job_crawler.company import get_companies

sys.path.insert(0, str(Path(__file__).parent.parent))

COMPANIES = get_companies()


@pytest.fixture(scope="session")
def event_loop():
	loop = asyncio.new_event_loop()
	yield loop
	loop.close()


@pytest.fixture(scope="session")
async def jobs_cache():
	async with aiohttp.ClientSession() as session:
		results = await asyncio.gather(
			*[company.board.get_jobs(session) for company in COMPANIES],
			return_exceptions=True,
		)
	return {company.name: result for company, result in zip(COMPANIES, results, strict=False)}
