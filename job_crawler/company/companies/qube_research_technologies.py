from job_crawler.board.boards.greenhouse import GreenHouse
from job_crawler.company.company import Company


class QubeResearchTechnologies(Company):
	name = "Qube Research & Technologies"
	logo_url = "https://upload.wikimedia.org/wikipedia/en/thumb/3/3f/Qube_Research_%26_Technologies_Logo.svg/1280px-Qube_Research_%26_Technologies_Logo.svg.png"
	website = "http://qube-rt.com/"

	@property
	def board(self) -> GreenHouse:
		return GreenHouse(board_token="quberesearchandtechnologies", company_name=self.name, company_logo_url=self.logo_url)
