from companies.base import Company
from engines import GreenHouse


class CapitalFundManagement(Company, GreenHouse):
	"""Greenhouse-backed engine for Capital Fund Management."""

	@property
	def name(self) -> str:
		"""Human-readable company name."""
		return "Capital Fund Management"

	@property
	def logo_url(self) -> str:
		"""URL of the company logo."""
		return "https://media.licdn.com/dms/image/v2/C4E0BAQHzx8gmbGG0Kg/company-logo_200_200/company-logo_200_200/0/1631344624809?e=2147483647&v=beta&t=zWstaZncYP53wGrc96oDPSGRpYLR37J0mqWpfrOz4hY"

	@property
	def website(self) -> str:
		"""Company website URL."""
		return "https://www.cfm.com/"

	@property
	def board_token(self) -> str:
		"""Greenhouse board token for Capital Fund Management."""
		return "cfm"
