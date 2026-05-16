import aiohttp
import pytest

from job_crawler.company.companies.n26 import N26


@pytest.fixture
def company():
	return N26()


@pytest.mark.asyncio
async def test_returns_jobs(company):
	async with aiohttp.ClientSession() as session:
		jobs = await company.board.get_jobs(session)
	assert isinstance(jobs, list)


@pytest.mark.asyncio
async def test_job_fields_populated(company):
	async with aiohttp.ClientSession() as session:
		jobs = await company.board.get_jobs(session)
	for job in jobs:
		assert job.id
		assert job.title
		assert job.link
		assert job.company_name == "N26"
