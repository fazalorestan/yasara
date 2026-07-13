from dataclasses import dataclass, field
from typing import Any
from app.platform_core.clock import utc_now_iso

@dataclass
class QueueMessage:
    id: str
    topic: str
    payload: dict[str, Any] = field(default_factory=dict)
    priority: int = 5
    attempts: int = 0
    created_at: str = field(default_factory=utc_now_iso)

@dataclass
class QueueDefinition:
    name: str
    max_size: int = 10000
    retry_enabled: bool = True
    dead_letter_enabled: bool = True
    mode: str = "report_only"

@dataclass
class WorkerContract:
    name: str
    queue: str
    enabled: bool = True
    mode: str = "contract_only"
