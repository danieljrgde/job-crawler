from job_crawler.board.boards.greenhouse import GreenHouse
from job_crawler.company.company import Company


class JaneStreet(Company):
	name = "Jane Street"
	logo_url = "https://logo.clearbit.com/janestreet.com"
	website = "https://www.janestreet.com/"

	@property
	def board(self) -> GreenHouse:
		return GreenHouse(board_token="janestreet", company_name=self.name, company_logo_url=self.logo_url)
