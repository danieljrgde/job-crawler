from pathlib import Path

import yaml

from job_crawler.board import BOARD_REGISTRY
from job_crawler.company.company import Company as Company

_COMPANIES_DIR = Path(__file__).parent / "companies"


def get_companies() -> list[Company]:
	return [
		Company(
			name=entry["name"],
			logo_url=entry["logo_url"],
			website=entry["website"],
			board_cls=BOARD_REGISTRY[entry["board"]],
			board_args=entry.get("board_args", {}),
		)
		for path in sorted(_COMPANIES_DIR.rglob("*.yaml"))
		for entry in [yaml.safe_load(path.read_text())]
	]
