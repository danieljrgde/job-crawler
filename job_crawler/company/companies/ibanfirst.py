from job_crawler.board.boards.greenhouse import GreenHouse
from job_crawler.company.company import Company


class IBanFirst(Company):
	name = "iBanFirst"
	logo_url = "https://logo.clearbit.com/ibanfirst.com"
	website = "https://www.ibanfirst.com/"

	@property
	def board(self) -> GreenHouse:
		return GreenHouse(board_token="ibanfirst", company_name=self.name, company_logo_url=self.logo_url)
