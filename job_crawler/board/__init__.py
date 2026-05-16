from job_crawler.board.board import Board as Board
from job_crawler.board.boards import GreenHouse as GreenHouse
from job_crawler.board.boards import Workday as Workday

BOARD_REGISTRY: dict[str, type[Board]] = {
	"greenhouse": GreenHouse,
	"workday": Workday,
}


def get_boards() -> list[type[Board]]:
	return list(Board.__subclasses__())
