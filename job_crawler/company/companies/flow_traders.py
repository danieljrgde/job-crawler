from job_crawler.board.boards.greenhouse import GreenHouse
from job_crawler.company.company import Company


class FlowTraders(Company):
    name = "Flow Traders"
    logo_url = "https://logo.clearbit.com/flowtraders.com"
    website = "https://www.flowtraders.com/"

    @property
    def board(self) -> GreenHouse:
        return GreenHouse(board_token="flowtraders", company_name=self.name, company_logo_url=self.logo_url)
