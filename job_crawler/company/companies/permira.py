from job_crawler.board.boards.greenhouse import GreenHouse
from job_crawler.company.company import Company


class Permira(Company):
	name = "Permira"
	logo_url = "https://logo.clearbit.com/permira.com"
	website = "https://www.permira.com/"

	@property
	def board(self) -> GreenHouse:
		return GreenHouse(board_token="permira", company_name=self.name, company_logo_url=self.logo_url)
