from job_crawler.board.boards.greenhouse import GreenHouse
from job_crawler.company.company import Company


class Optiver(Company):
	name = "Optiver"
	logo_url = "https://logo.clearbit.com/optiver.com"
	website = "https://optiver.com/"

	@property
	def board(self) -> GreenHouse:
		return GreenHouse(board_token="optiver", company_name=self.name, company_logo_url=self.logo_url)
