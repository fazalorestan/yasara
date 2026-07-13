from datetime import datetime, timezone
from enum import StrEnum
from pydantic import BaseModel, Field

class DashboardHealthStatus(StrEnum):
    OK = "ok"
    DEGRADED = "degraded"
    DOWN = "down"

class DashboardWidgetType(StrEnum):
    SYSTEM = "system"
    PORTFOLIO = "portfolio"
    SIGNALS = "signals"
    RISK = "risk"
    STRATEGIES = "strategies"
    NOTIFICATIONS = "notifications"
    EXCHANGE = "exchange"

class DashboardMetric(BaseModel):
    key: str
    label: str
    value: float | int | str | bool
    unit: str = ""
    precision: int = 2

class DashboardPanel(BaseModel):
    panel_id: str
    title: str
    widget_type: DashboardWidgetType
    metrics: list[DashboardMetric] = Field(default_factory=list)
    payload: dict = Field(default_factory=dict)
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class DashboardSystemStatus(BaseModel):
    service: str = "yasara-backend"
    status: DashboardHealthStatus = DashboardHealthStatus.OK
    version: str = "sprint15"
    uptime_seconds: float = 0
    modules: dict[str, DashboardHealthStatus] = Field(default_factory=dict)
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class DashboardWatchlistItem(BaseModel):
    symbol: str
    price: float = 0
    change_percent: float = 0
    confidence: float = 0
    status: str = "watching"

class DashboardStrategyItem(BaseModel):
    strategy_id: str
    name: str
    status: str
    version: int
    last_score: float = 0

class DashboardSignalItem(BaseModel):
    symbol: str
    direction: str
    confidence: float
    quality: float = 0
    reason: str = ""

class DashboardSnapshot(BaseModel):
    system: DashboardSystemStatus
    panels: list[DashboardPanel] = Field(default_factory=list)
    watchlist: list[DashboardWatchlistItem] = Field(default_factory=list)
    strategies: list[DashboardStrategyItem] = Field(default_factory=list)
    signals: list[DashboardSignalItem] = Field(default_factory=list)
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
