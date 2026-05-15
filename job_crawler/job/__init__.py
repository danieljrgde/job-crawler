import asyncio

import aiohttp

from job_crawler.job.job import Job


async def get_jobs(companies=None, timeout: int = 30) -> list[Job]:
    if companies is None:
        from job_crawler.company import get_companies
        companies = get_companies()
    client_timeout = aiohttp.ClientTimeout(total=timeout)
    async with aiohttp.ClientSession(timeout=client_timeout) as session:
        results = await asyncio.gather(*(c.get_jobs(session) for c in companies))
    return [job for roles in results for job in roles]
