from typing import Any
from pydantic import BaseModel, Field

class ProviderState(BaseModel):
    name: str
    available: bool
    source: str
    payload: dict[str, Any] = Field(default_factory=dict)
    error: str | None = None

class ApprovedDashboardSnapshot(BaseModel):
    build_id: str = "2026.47.ENTERPRISE.001"
    approved_dashboard_locked: bool = True
    real_data_only: bool = True
    mock_data: bool = False
    signal_only_default: bool = True
    auto_trading_enabled: bool = False
    providers: list[ProviderState] = Field(default_factory=list)
    widgets: dict[str, Any] = Field(default_factory=dict)
