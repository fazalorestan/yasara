from pydantic import BaseModel, Field
from time import time
from typing import Any


class DashboardPanelV11(BaseModel):
    key: str
    title: str
    status: str = "ready"
    payload: dict[str, Any] = Field(default_factory=dict)


class DashboardAlertV11(BaseModel):
    level: str
    message: str
    source: str
    timestamp: float = Field(default_factory=time)


class DashboardRuntimeSnapshotV11(BaseModel):
    ready: bool
    version: str = "1.1.0-phase4"
    panels: list[DashboardPanelV11] = Field(default_factory=list)
    alerts: list[DashboardAlertV11] = Field(default_factory=list)
    timestamp: float = Field(default_factory=time)


class DashboardSummaryV11(BaseModel):
    ready: bool
    panel_count: int
    alert_count: int
    sources: list[str] = Field(default_factory=list)
