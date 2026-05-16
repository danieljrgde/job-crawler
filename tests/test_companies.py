import pytest

from conftest import COMPANIES


@pytest.mark.parametrize("company", COMPANIES, ids=lambda c: c.name)
async def test_returns_jobs(company, jobs_cache):
	jobs = jobs_cache[company.name]
	if isinstance(jobs, Exception):
		raise jobs
	assert isinstance(jobs, list)


@pytest.mark.parametrize("company", COMPANIES, ids=lambda c: c.name)
async def test_job_fields_populated(company, jobs_cache):
	jobs = jobs_cache[company.name]
	if isinstance(jobs, Exception):
		raise jobs
	for job in jobs:
		assert job.id
		assert job.title
		assert job.link
		assert job.company_name == company.name
