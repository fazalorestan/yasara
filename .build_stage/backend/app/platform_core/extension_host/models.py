from dataclasses import dataclass, field
from typing import Any

PLUGIN_RUNTIME_STATES = [
    "created",
    "starting",
    "running",
    "busy",
    "slow",
    "warning",
    "error",
    "recovering",
    "paused",
    "disabled",
    "stopping",
    "stopped",
]

@dataclass
class PluginRuntimeInfo:
    name: str
    state: str = "created"
    startup_ms: float = 0.0
    health: str = "healthy"
    detail: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class ResourceQuota:
    cpu_percent: float = 25.0
    memory_mb: int = 512
    threads: int = 4
    api_calls_per_minute: int = 120
    events_per_minute: int = 300
    mode: str = "report_only"
