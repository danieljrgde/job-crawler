from job_crawler.board.boards.greenhouse import GreenHouse
from job_crawler.company.company import Company


class Stripe(Company):
    name = "Stripe"
    logo_url = "https://logo.clearbit.com/stripe.com"
    website = "https://stripe.com/"

    @property
    def board(self) -> GreenHouse:
        return GreenHouse(board_token="stripe", company_name=self.name, company_logo_url=self.logo_url)
