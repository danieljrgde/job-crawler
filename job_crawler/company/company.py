from abc import ABC, abstractmethod

from job_crawler.board.board import Board


class Company(ABC):
    """A company whose job postings we crawl."""

    name: str
    logo_url: str
    website: str

    @property
    @abstractmethod
    def board(self) -> Board:
        """The job board integration used to fetch this company's postings."""
        ...
