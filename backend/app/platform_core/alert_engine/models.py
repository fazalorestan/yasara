from dataclasses import dataclass, field
from typing import Any
from app.platform_core.clock import utc_now_iso

@dataclass
class AlertRule:
    rule_id: str
    name: str
    condition: str
    severity: str = "info"
    enabled: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class AlertEvent:
    rule_id: str
    symbol: str
    message: str
    severity: str
    triggered_at: str = field(default_factory=utc_now_iso)
    acknowledged: bool = False

@dataclass
class NotificationContract:
    channel: str
    enabled: bool = False
    dry_run: bool = True
