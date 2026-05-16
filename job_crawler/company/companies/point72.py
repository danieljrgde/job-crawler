from job_crawler.board.boards.greenhouse import GreenHouse
from job_crawler.company.company import Company


class Point72(Company):
	name = "Point72"
	logo_url = "https://media.glassdoor.com/sqll/1032703/point72-squareLogo-1732725839273.png"
	website = "https://point72.com/"

	@property
	def board(self) -> GreenHouse:
		return GreenHouse(board_token="point72", company_name=self.name, company_logo_url=self.logo_url)
