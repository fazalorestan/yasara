from pydantic import BaseModel, Field
from app.v11_dashboard_runtime.snapshot_service import DashboardRuntimeServiceV11


class V11Phase4Summary(BaseModel):
    ready: bool
    phase: str = "v1_1_phase_4_dashboard_runtime_api"
    capabilities: list[str] = Field(default_factory=list)
    safety: str = "dashboard_read_only_no_order_execution"


class V11Phase4SummaryBuilder:
    def build(self) -> V11Phase4Summary:
        summary = DashboardRuntimeServiceV11().summary()
        return V11Phase4Summary(
            ready=summary.ready and summary.panel_count >= 3,
            capabilities=[
                "market_snapshot_panel",
                "exchange_connectivity_panel",
                "ai_market_intelligence_panel",
                "dashboard_alerts",
                "dashboard_summary",
                "unified_dashboard_snapshot_api",
            ],
        )
