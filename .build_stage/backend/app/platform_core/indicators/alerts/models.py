from dataclasses import dataclass, field
from typing import Any
from app.platform_core.clock import utc_now_iso

@dataclass
class IndicatorAlertPayload:
    id: str
    indicator: str = "yasara"
    symbol: str = "UNKNOWN"
    direction: str = "WAIT"
    confidence: int = 0
    severity: str = "info"
    message: str = ""
    created_at: str = field(default_factory=utc_now_iso)
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class IndicatorAlertPolicy:
    min_confidence: int = 65
    dedupe_window_seconds: int = 300
    mode: str = "analysis_only"
