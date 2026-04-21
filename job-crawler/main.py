"""Entry point for the job crawler."""

import argparse
import asyncio
import json

import aiohttp
from engines import Job
from utils.helpers import all_companies


async def crawl_jobs(timeout_in_seconds: int) -> list[Job]:
	"""Crawl every known company concurrently and return the flattened job list."""
	companies = all_companies()
	timeout = aiohttp.ClientTimeout(total=timeout_in_seconds)
	async with aiohttp.ClientSession(timeout=timeout) as session:
		results = await asyncio.gather(*(c.get_jobs(session) for c in companies))
	return [job for roles in results for job in roles]


def _parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description="Crawl job postings from known companies.")
	parser.add_argument(
		"--timeout",
		type=int,
		default=30,
		help="HTTP request timeout in seconds (default: 30).",
	)
	return parser.parse_args()


if __name__ == "__main__":
	args = _parse_args()
	jobs = asyncio.run(crawl_jobs(args.timeout))
	print(json.dumps(jobs, indent=2, default=str))  # noqa: T201
