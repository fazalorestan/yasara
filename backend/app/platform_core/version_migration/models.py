from dataclasses import dataclass, field
from typing import Any

@dataclass
class PlatformVersionRecord:
    version: str
    title: str
    category: str = "platform"
    status: str = "active"
    notes: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class MigrationPlan:
    from_version: str
    to_version: str
    title: str
    steps: list[str] = field(default_factory=list)
    destructive: bool = False
    status: str = "planned"

@dataclass
class CompatibilityLedgerEntry:
    item: str
    compatible: bool = True
    deprecated: bool = False
    replacement: str = ""
    notes: str = ""
