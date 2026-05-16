from job_crawler.board.boards.greenhouse import GreenHouse
from job_crawler.company.company import Company


class AlixPartners(Company):
    name = "AlixPartners"
    logo_url = "https://logo.clearbit.com/alixpartners.com"
    website = "https://www.alixpartners.com/"

    @property
    def board(self) -> GreenHouse:
        return GreenHouse(board_token="alixpartners", company_name=self.name, company_logo_url=self.logo_url)
