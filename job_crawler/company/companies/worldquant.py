from job_crawler.board.boards.greenhouse import GreenHouse
from job_crawler.company.company import Company


class WorldQuant(Company):
    name = "WorldQuant"
    logo_url = "https://logo.clearbit.com/worldquant.com"
    website = "https://www.worldquant.com/"

    @property
    def board(self) -> GreenHouse:
        return GreenHouse(board_token="worldquant", company_name=self.name, company_logo_url=self.logo_url)
