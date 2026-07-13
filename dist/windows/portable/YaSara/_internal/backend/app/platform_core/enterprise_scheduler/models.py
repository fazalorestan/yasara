from dataclasses import dataclass, field
from typing import Any
from app.platform_core.clock import utc_now_iso

@dataclass
class ScheduledJob:
    name: str
    interval_seconds: int = 60
    enabled: bool = True
    cron: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=utc_now_iso)

@dataclass
class RetryPolicy:
    max_retries: int = 3
    backoff_seconds: int = 10
    mode: str = "report_only"

@dataclass
class TaskStatus:
    name: str
    status: str = "registered"
    last_run_at: str = ""
    run_count: int = 0
    error_count: int = 0
