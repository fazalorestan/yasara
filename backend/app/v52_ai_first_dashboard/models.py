from __future__ import annotations
from typing import Any
from pydantic import BaseModel, Field

class DashboardMetric(BaseModel):
    key: str
    label: str
    value: Any = None
    status: str = "unavailable"
    source: str
    updated_at: float | None = None

class DashboardSection(BaseModel):
    key: str
    title: str
    status: str = "unavailable"
    source: str
    payload: dict[str, Any] = Field(default_factory=dict)

class AIFirstDashboardSnapshot(BaseModel):
    build_id: str = "2026.45.ENTERPRISE.001"
    ready: bool = True
    real_data_only: bool = True
    mock_data: bool = False
    signal_only_default: bool = True
    auto_trading_enabled: bool = False
    metrics: list[DashboardMetric] = Field(default_factory=list)
    sections: list[DashboardSection] = Field(default_factory=list)
    doctor: dict[str, Any] = Field(default_factory=dict)
