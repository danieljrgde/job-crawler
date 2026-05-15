from job_crawler.company.company import Company
from job_crawler.company.companies.capital_fund_management import CapitalFundManagement
from job_crawler.company.companies.point72 import Point72
from job_crawler.company.companies.qube_research_technologies import QubeResearchTechnologies


def get_companies() -> list[Company]:
    return [cls() for cls in Company.__subclasses__() if not cls.__abstractmethods__]
