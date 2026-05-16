from job_crawler.board.boards.greenhouse import GreenHouse
from job_crawler.company.company import Company


class JumpTrading(Company):
	name = "Jump Trading"
	logo_url = "https://logo.clearbit.com/jumptrading.com"
	website = "https://www.jumptrading.com/"

	@property
	def board(self) -> GreenHouse:
		return GreenHouse(board_token="jumptrading", company_name=self.name, company_logo_url=self.logo_url)
