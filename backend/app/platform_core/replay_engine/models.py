from dataclasses import dataclass, field
from typing import Any
from app.platform_core.clock import utc_now_iso

@dataclass
class ReplaySession:
    session_id: str
    symbol: str
    timeframe: str
    speed: float = 1.0
    cursor: int = 0
    playing: bool = False
    created_at: str = field(default_factory=utc_now_iso)

@dataclass
class ReplayEvent:
    index: int
    event_type: str
    payload: dict[str, Any]
    timestamp: str = field(default_factory=utc_now_iso)

@dataclass
class ReplayPlaybackState:
    session_id: str
    cursor: int
    total_events: int
    playing: bool
    speed: float
