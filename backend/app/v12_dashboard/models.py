from pydantic import BaseModel, Field


class DashboardAssetV12(BaseModel):
    name: str
    path: str
    required: bool = True


class DashboardShellSummaryV12(BaseModel):
    ready: bool
    version: str = "1.2.0-phase1"
    progress_percent: int = 20
    route: str = "/app"
    assets: list[DashboardAssetV12] = Field(default_factory=list)
    safety: str = "dashboard_only_no_live_trading"
