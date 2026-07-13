from __future__ import annotations
from typing import Any
from pydantic import BaseModel, Field

class WorkspaceDescriptor(BaseModel):
    id: str
    title: str
    icon: str
    order: int
    enabled: bool = True
    route: str
    source: str
    health: str = "unknown"
    permissions: list[str] = Field(default_factory=list)
    capabilities: list[str] = Field(default_factory=list)

class WorkspaceRegistrySnapshot(BaseModel):
    build_id: str = "2026.46.ENTERPRISE.001"
    real_data_only: bool = True
    mock_data: bool = False
    dashboard_layout_locked: bool = True
    workspaces: list[WorkspaceDescriptor] = Field(default_factory=list)
    doctor: dict[str, Any] = Field(default_factory=dict)
