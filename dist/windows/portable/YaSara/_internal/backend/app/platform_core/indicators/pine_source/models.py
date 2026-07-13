from dataclasses import dataclass, field
from typing import Any
from app.platform_core.clock import utc_now_iso

@dataclass
class PineSourceRecord:
    indicator: str
    version: str
    title: str
    source_path: str
    archived_at: str = field(default_factory=utc_now_iso)
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class PineUpdateSafetyContract:
    editable_file: str
    stable_runtime_files: list[str]
    rules: list[str]
    destructive: bool = False
    mode: str = "contract_only"

@dataclass
class PineRuntimeMapping:
    pine_section: str
    runtime_target: str
    status: str = "mapped"
