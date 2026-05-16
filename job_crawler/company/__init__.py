from pathlib import Path

import yaml

from job_crawler.board import BOARD_REGISTRY
from job_crawler.company.company import Company as Company

_YAML = Path(__file__).parent / "companies.yaml"


def get_companies() -> list[Company]:
	data = yaml.safe_load(_YAML.read_text())
	return [
		Company(
			name=entry["name"],
			logo_url=entry["logo_url"],
			website=entry["website"],
			board_cls=BOARD_REGISTRY[entry["board"]],
			board_args=entry.get("board_args", {}),
		)
		for entry in data
	]
