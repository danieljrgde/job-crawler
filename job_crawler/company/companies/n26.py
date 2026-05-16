from job_crawler.board.boards.greenhouse import GreenHouse
from job_crawler.company.company import Company


class N26(Company):
    name = "N26"
    logo_url = "https://logo.clearbit.com/n26.com"
    website = "https://n26.com/"

    @property
    def board(self) -> GreenHouse:
        return GreenHouse(board_token="n26", company_name=self.name, company_logo_url=self.logo_url)
