from __future__ import annotations

from typing import Any, Literal
from pydantic import BaseModel, Field


WorkspaceName = Literal["trader", "ai", "portfolio", "developer"]


class MetricValue(BaseModel):
    key: str
    label: str
    value: Any = None
    status: str = "unavailable"
    source: str
    updated_at: float | None = None


class WorkspaceSnapshot(BaseModel):
    workspace: WorkspaceName
    ready: bool = True
    metrics: list[MetricValue] = Field(default_factory=list)
    panels: dict[str, Any] = Field(default_factory=dict)


class TradingOSSnapshot(BaseModel):
    build_id: str = "2026.43.ENTERPRISE.001"
    ready: bool = True
    real_data_only: bool = True
    mock_data: bool = False
    signal_only_default: bool = True
    auto_trading_enabled: bool = False
    workspaces: list[WorkspaceSnapshot] = Field(default_factory=list)
    doctor: dict[str, Any] = Field(default_factory=dict)
    runtime: dict[str, Any] = Field(default_factory=dict)
