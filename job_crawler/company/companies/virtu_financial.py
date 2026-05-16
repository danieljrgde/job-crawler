from job_crawler.board.boards.greenhouse import GreenHouse
from job_crawler.company.company import Company


class VirtuFinancial(Company):
	name = "Virtu Financial"
	logo_url = "https://logo.clearbit.com/virtu.com"
	website = "https://www.virtu.com/"

	@property
	def board(self) -> GreenHouse:
		return GreenHouse(board_token="virtu", company_name=self.name, company_logo_url=self.logo_url)
