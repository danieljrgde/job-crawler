from job_crawler.board.boards.greenhouse import GreenHouse
from job_crawler.company.company import Company


class EQTPartners(Company):
	name = "EQT Partners"
	logo_url = "https://logo.clearbit.com/eqtgroup.com"
	website = "https://eqtgroup.com/"

	@property
	def board(self) -> GreenHouse:
		return GreenHouse(board_token="eqtpartners", company_name=self.name, company_logo_url=self.logo_url)
