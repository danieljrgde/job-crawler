from job_crawler.board.boards.greenhouse import GreenHouse
from job_crawler.company.company import Company


class ShiftTechnology(Company):
    name = "Shift Technology"
    logo_url = "https://logo.clearbit.com/shift-technology.com"
    website = "https://www.shift-technology.com/"

    @property
    def board(self) -> GreenHouse:
        return GreenHouse(board_token="shifttechnology", company_name=self.name, company_logo_url=self.logo_url)
