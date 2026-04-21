from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from jobs import Job

if TYPE_CHECKING:
	import aiohttp


class Engine(ABC):
	"""Abstract base class for job board engines.

	Each subclass represents a single company or job board integration
	and knows how to fetch that source's current job postings. Engines
	are designed to run concurrently against a shared ``aiohttp`` session.
	"""

	@abstractmethod
	async def get_jobs(self, session: aiohttp.ClientSession) -> list[Job]:
		"""Return the current list of job postings from this engine.

		Implementations should handle their own network and parsing
		errors and return an empty list on failure, so that one failing
		engine does not disrupt a concurrent crawl.
		"""
		...
