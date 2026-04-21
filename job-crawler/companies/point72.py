from companies.base import Company
from engines import GreenHouse


class Point72(Company, GreenHouse):
	"""Greenhouse-backed engine for Point72."""

	@property
	def name(self) -> str:
		"""Human-readable company name."""
		return "Point72"

	@property
	def logo_url(self) -> str:
		"""URL of the company logo."""
		return "https://media.glassdoor.com/sqll/1032703/point72-squareLogo-1732725839273.png"

	@property
	def website(self) -> str:
		"""Company website URL."""
		return "https://point72.com/"

	@property
	def board_token(self) -> str:
		"""Greenhouse board token for Point72."""
		return "point72"
