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
import asyncio
from job_crawler import get_companies, get_jobs

companies = [c for c in get_companies() if c.name in {"Adyen", "Stripe"}]
jobs = asyncio.run(get_jobs(companies=companies))
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

Add a new file under [job_crawler/board/boards/](job_crawler/board/boards/) implementing the `Board` abstract class, then export it from [job_crawler/board/boards/\_\_init\_\_.py](job_crawler/board/boards/__init__.py) and register it in `BOARD_REGISTRY` in [job_crawler/board/\_\_init\_\_.py](job_crawler/board/__init__.py).

**3. Add the company to [job_crawler/company/companies.yaml](job_crawler/company/companies.yaml).**

```yaml
- name: Acme Corp
  logo_url: https://logo.clearbit.com/acme.com
  website: https://acme.com/
  board: greenhouse
  board_args:
    board_token: acmecorp
```

The `board_token` is the slug from the Greenhouse URL: `boards.greenhouse.io/<board_token>`. For other boards, `board_args` accepts whatever the board's constructor requires.

That's it — no new Python file, no new test file. The parameterized test suite in [tests/test_companies.py](tests/test_companies.py) picks up the new entry automatically.
