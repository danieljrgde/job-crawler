# job-crawler

Crawls job postings from company career pages and returns them as structured `Job` objects. Currently supports companies using [Greenhouse](https://www.greenhouse.com/) and [Workday](https://www.workday.com/) job boards.

## Setup

Requires Python 3.13+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync --group dev
```

## Usage

```python
import asyncio
from job_crawler import get_jobs

jobs = asyncio.run(get_jobs())
for job in jobs:
    print(job)
```

You can also pass a subset of companies:

```python
from job_crawler import get_jobs
from job_crawler.company.companies.adyen import Adyen
from job_crawler.company.companies.stripe import Stripe

jobs = asyncio.run(get_jobs(companies=[Adyen(), Stripe()]))
```

## Running tests

```bash
pytest tests/
```

## Contributing

### Adding a new company

**1. Check which job board the company uses.**

Look at the company's careers page URL. Supported boards:

| Board | URL pattern |
|---|---|
| Greenhouse | `boards.greenhouse.io/<token>` |
| Workday | `<company>.wd<n>.myworkdayjobs.com` |

**2. If the board is not yet supported, create it.**

Add a new file under [job_crawler/board/boards/](job_crawler/board/boards/) implementing the `Board` abstract class, then export it from [job_crawler/board/boards/\_\_init\_\_.py](job_crawler/board/boards/__init__.py).

**3. Create the company class.**

Add a file under [job_crawler/company/companies/](job_crawler/company/companies/) following this pattern:

```python
from job_crawler.board.boards.greenhouse import GreenHouse
from job_crawler.company.company import Company


class Acme(Company):
    name = "Acme Corp"
    logo_url = "https://logo.clearbit.com/acme.com"
    website = "https://acme.com/"

    @property
    def board(self) -> GreenHouse:
        return GreenHouse(board_token="acmecorp", company_name=self.name, company_logo_url=self.logo_url)
```

The `board_token` is the slug that appears in the Greenhouse URL: `boards.greenhouse.io/<board_token>`.

**4. Register the company.**

Add an export to both [job_crawler/company/companies/\_\_init\_\_.py](job_crawler/company/companies/__init__.py) and [job_crawler/company/\_\_init\_\_.py](job_crawler/company/__init__.py):

```python
from job_crawler.company.companies.acme import Acme as Acme
```

**5. Add tests.**

Create [tests/test_acme.py](tests/test_acme.py) following the existing pattern:

```python
import aiohttp
import pytest
from job_crawler.company.companies.acme import Acme


@pytest.fixture
def company():
    return Acme()


@pytest.mark.asyncio
async def test_returns_jobs(company):
    async with aiohttp.ClientSession() as session:
        jobs = await company.board.get_jobs(session)
    assert isinstance(jobs, list)


@pytest.mark.asyncio
async def test_job_fields_populated(company):
    async with aiohttp.ClientSession() as session:
        jobs = await company.board.get_jobs(session)
    for job in jobs:
        assert job.id
        assert job.title
        assert job.link
        assert job.company_name == "Acme Corp"
```
