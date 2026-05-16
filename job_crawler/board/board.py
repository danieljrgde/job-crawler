from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import aiohttp

    from job_crawler.job.job import Job


class Board(ABC):
	"""Abstract base class for job board integrations.

	Each subclass represents a single job board and knows how to fetch its
	current job postings. Boards are designed to run concurrently against
	a shared ``aiohttp`` session.
	"""

	@abstractmethod
	async def get_jobs(self, session: aiohttp.ClientSession) -> list[Job]:
		"""Return the current list of job postings from this board.

		Implementations should handle their own network and parsing errors
		and return an empty list on failure, so that one failing board does
		not disrupt a concurrent crawl.
		"""
		...
