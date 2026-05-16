from job_crawler.board.boards.greenhouse import GreenHouse
from job_crawler.company.company import Company


class CapitalFundManagement(Company):
	name = "Capital Fund Management"
	logo_url = "https://media.licdn.com/dms/image/v2/C4E0BAQHzx8gmbGG0Kg/company-logo_200_200/company-logo_200_200/0/1631344624809?e=2147483647&v=beta&t=zWstaZncYP53wGrc96oDPSGRpYLR37J0mqWpfrOz4hY"
	website = "https://www.cfm.com/"

	@property
	def board(self) -> GreenHouse:
		return GreenHouse(board_token="cfm", company_name=self.name, company_logo_url=self.logo_url)
