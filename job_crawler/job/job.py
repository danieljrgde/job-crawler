"""Data models for job postings crawled from company boards."""

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum

# ------------------------------ #
# --- ENUMS -------------------- #
# ------------------------------ #


class ContractType(StrEnum):
	"""Supported employment contract types."""

	full_time = "Full-time"
	part_time = "Part-time"
	internship = "Internship"
	apprenticeship = "Apprenticeship"


class WorkMode(StrEnum):
	"""Supported remote/onsite working modes."""

	remote = "Remote"
	hybrid = "Hybrid"
	onsite = "Onsite"


# ------------------------------ #
# --- DATACLASS ---------------- #
# ------------------------------ #


@dataclass(frozen=True)
class Location:
	"""A job posting location; parts not exposed by a board are ``None``."""

	country: str | None
	state: str | None
	city: str | None


@dataclass(frozen=True)
class Job:
	"""A single job posting."""

	id: str
	title: str
	description: str
	department: str | None
	location: list[Location]
	date_posted: datetime | None
	date_modified: datetime | None
	contract_type: ContractType | None
	company_name: str
	company_logo_url: str
	work_mode: WorkMode | None
	link: str

	def __str__(self) -> str:
		"""Return a short human-readable label for this job."""
		return f"{self.title} @ {self.company_name}"
