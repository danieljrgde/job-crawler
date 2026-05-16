from job_crawler.board.boards.greenhouse import GreenHouse
from job_crawler.company.company import Company


class TowerResearchCapital(Company):
    name = "Tower Research Capital"
    logo_url = "https://logo.clearbit.com/tower-research.com"
    website = "https://tower-research.com/"

    @property
    def board(self) -> GreenHouse:
        return GreenHouse(board_token="towerresearchcapital", company_name=self.name, company_logo_url=self.logo_url)
