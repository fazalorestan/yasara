import time
from app.dashboard_v1.domain.models import DashboardHealthStatus, DashboardSystemStatus

class DashboardSystemStatusEngineV1:
    def __init__(self):
        self.started_at = time.monotonic()

    def build(self) -> DashboardSystemStatus:
        return DashboardSystemStatus(
            status=DashboardHealthStatus.OK,
            uptime_seconds=max(0, time.monotonic() - self.started_at),
            modules={
                "exchange": DashboardHealthStatus.OK,
                "market_data": DashboardHealthStatus.OK,
                "decision": DashboardHealthStatus.OK,
                "risk": DashboardHealthStatus.OK,
                "paper_trading": DashboardHealthStatus.OK,
                "notifications": DashboardHealthStatus.OK,
                "secrets": DashboardHealthStatus.OK,
                "account_sync": DashboardHealthStatus.OK,
                "strategy_builder": DashboardHealthStatus.OK,
            },
        )
