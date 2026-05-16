from job_crawler.board.boards.greenhouse import GreenHouse
from job_crawler.company.company import Company


class Adyen(Company):
	name = "Adyen"
	logo_url = "https://logo.clearbit.com/adyen.com"
	website = "https://www.adyen.com/"

	@property
	def board(self) -> GreenHouse:
		return GreenHouse(board_token="adyen", company_name=self.name, company_logo_url=self.logo_url)
