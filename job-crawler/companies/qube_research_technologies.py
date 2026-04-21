from companies.base import Company
from engines import GreenHouse


class QubeResearchTechnologies(Company, GreenHouse):
	"""Greenhouse-backed engine for Qube Research & Technologies."""

	@property
	def name(self) -> str:
		"""Human-readable company name."""
		return "Qube Research & Technologies"

	@property
	def logo_url(self) -> str:
		"""URL of the company logo."""
		return "https://upload.wikimedia.org/wikipedia/en/thumb/3/3f/Qube_Research_%26_Technologies_Logo.svg/1280px-Qube_Research_%26_Technologies_Logo.svg.png"

	@property
	def website(self) -> str:
		"""Company website URL."""
		return "http://qube-rt.com/"

	@property
	def board_token(self) -> str:
		"""Greenhouse board token for Qube Research & Technologies."""
		return "quberesearchandtechnologies"
