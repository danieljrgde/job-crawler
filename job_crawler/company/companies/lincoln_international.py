from job_crawler.board.boards.greenhouse import GreenHouse
from job_crawler.company.company import Company


class LincolnInternational(Company):
	name = "Lincoln International"
	logo_url = "https://logo.clearbit.com/lincolninternational.com"
	website = "https://lincolninternational.com/"

	@property
	def board(self) -> GreenHouse:
		return GreenHouse(board_token="lincolninternational", company_name=self.name, company_logo_url=self.logo_url)
