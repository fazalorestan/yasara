from dataclasses import dataclass, field
from app.platform_core.clock import utc_now_iso

@dataclass
class IndicatorLifecycleState:
    indicator: str
    state: str = "discovered"
    version: str = "v1.0"
    updated_at: str = field(default_factory=utc_now_iso)

@dataclass
class IndicatorLifecycleTransition:
    indicator: str
    from_state: str
    to_state: str
    allowed: bool
    reason: str = ""
