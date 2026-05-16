from job_crawler.board.boards.greenhouse import GreenHouse
from job_crawler.company.company import Company


class Alma(Company):
	name = "Alma"
	logo_url = "https://logo.clearbit.com/getalma.eu"
	website = "https://getalma.eu/"

	@property
	def board(self) -> GreenHouse:
		return GreenHouse(board_token="alma31", company_name=self.name, company_logo_url=self.logo_url)
