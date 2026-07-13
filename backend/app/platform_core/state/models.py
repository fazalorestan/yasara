from dataclasses import dataclass, field
from typing import Any
from app.platform_core.clock import utc_now_iso

@dataclass
class PluginStateRecord:
    plugin: str
    state: dict[str, Any] = field(default_factory=dict)
    version: str = "v4.29"
    updated_at: str = field(default_factory=utc_now_iso)

@dataclass
class RuntimeSnapshot:
    snapshot_id: str
    plugins: dict[str, dict[str, Any]] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=utc_now_iso)
