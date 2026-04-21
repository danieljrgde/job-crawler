"""Helpers for enumerating the companies whose job boards we crawl."""

from companies import CapitalFundManagement, Company, Point72, QubeResearchTechnologies


def all_companies() -> list[Company]:
	"""Return one instance of every concrete ``Company`` we crawl."""
	return [QubeResearchTechnologies(), Point72(), CapitalFundManagement()]
