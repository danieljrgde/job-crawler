from job_crawler.board.boards.greenhouse import GreenHouse
from job_crawler.company.company import Company


class SquarepointCapital(Company):
	name = "Squarepoint Capital"
	logo_url = "https://logo.clearbit.com/squarepoint-capital.com"
	website = "https://www.squarepoint-capital.com/"

	@property
	def board(self) -> GreenHouse:
		return GreenHouse(board_token="squarepointcapital", company_name=self.name, company_logo_url=self.logo_url)
