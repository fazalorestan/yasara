from pydantic import BaseModel, Field

class DashboardFeedItemV1(BaseModel):
    key: str
    title: str
    value: str | float | int
    severity: str = "info"

class DashboardFeedV1(BaseModel):
    items: list[DashboardFeedItemV1] = Field(default_factory=list)

class DashboardFeedBuilderV1:
    def build_basic(self, total_symbols: int, active_exchanges: int, alerts_triggered: int = 0) -> DashboardFeedV1:
        return DashboardFeedV1(items=[
            DashboardFeedItemV1(key="symbols", title="Symbols", value=total_symbols),
            DashboardFeedItemV1(key="exchanges", title="Active Exchanges", value=active_exchanges),
            DashboardFeedItemV1(key="alerts", title="Alerts Triggered", value=alerts_triggered, severity="warning" if alerts_triggered else "info"),
        ])
