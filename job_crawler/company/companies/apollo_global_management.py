from job_crawler.board.boards.greenhouse import GreenHouse
from job_crawler.company.company import Company


class ApolloGlobalManagement(Company):
	name = "Apollo Global Management"
	logo_url = "https://logo.clearbit.com/apollo.com"
	website = "https://www.apollo.com/"

	@property
	def board(self) -> GreenHouse:
		return GreenHouse(board_token="apollo", company_name=self.name, company_logo_url=self.logo_url)
