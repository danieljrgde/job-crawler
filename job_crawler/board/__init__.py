from job_crawler.board.board import Board
from job_crawler.board.boards import GreenHouse, Workday


def get_boards() -> list[type[Board]]:
    return list(Board.__subclasses__())