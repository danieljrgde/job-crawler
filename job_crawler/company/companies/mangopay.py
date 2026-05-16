from job_crawler.board.boards.greenhouse import GreenHouse
from job_crawler.company.company import Company


class Mangopay(Company):
    name = "Mangopay"
    logo_url = "https://logo.clearbit.com/mangopay.com"
    website = "https://mangopay.com/"

    @property
    def board(self) -> GreenHouse:
        return GreenHouse(board_token="mangopay", company_name=self.name, company_logo_url=self.logo_url)
