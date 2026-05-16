from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from job_crawler.board.board import Board


class Company:
	"""A company whose job postings we crawl."""

	def __init__(self, *, name: str, logo_url: str, website: str, board_cls: type[Board], board_args: dict) -> None:
		self.name = name
		self.logo_url = logo_url
		self.website = website
		self._board_cls = board_cls
		self._board_args = board_args

	@property
	def board(self) -> Board:
		return self._board_cls(company_name=self.name, company_logo_url=self.logo_url, **self._board_args)
