from abc import ABC, abstractmethod


class Company(ABC):
	"""A company whose job postings we crawl.

	Concrete subclasses mix in a ``Board`` implementation (e.g. ``GreenHouse``)
	and provide the source-specific configuration plus company metadata.
	"""

	@property
	@abstractmethod
	def name(self) -> str:
		"""Human-readable name, e.g. ``"Qube Research & Technologies"``."""

	@property
	@abstractmethod
	def logo_url(self) -> str:
		"""URL of the company logo, e.g. ``"https://qube-rt.com/logo.png"``."""

	@property
	@abstractmethod
	def website(self) -> str:
		"""Company website URL, e.g. ``"http://qube-rt.com/"``."""
