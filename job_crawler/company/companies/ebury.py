from job_crawler.board.boards.greenhouse import GreenHouse
from job_crawler.company.company import Company


class Ebury(Company):
    name = "Ebury"
    logo_url = "https://logo.clearbit.com/ebury.com"
    website = "https://ebury.com/"

    @property
    def board(self) -> GreenHouse:
        return GreenHouse(board_token="ebury", company_name=self.name, company_logo_url=self.logo_url)
