from app.dashboard_v1.domain.models import DashboardSignalItem, DashboardSnapshot, DashboardStrategyItem
from app.dashboard_v1.engine.panel_builder import DashboardPanelBuilderV1
from app.dashboard_v1.engine.system_status import DashboardSystemStatusEngineV1
from app.dashboard_v1.engine.watchlist import DashboardWatchlistEngineV1
from app.notifications_v1.application.service import notification_service_v1
from app.strategy_builder_v1.application.service import strategy_builder_service_v1

class DashboardSnapshotBuilderV1:
    def __init__(self):
        self.system = DashboardSystemStatusEngineV1()
        self.panels = DashboardPanelBuilderV1()
        self.watchlist = DashboardWatchlistEngineV1()

    async def build(self) -> DashboardSnapshot:
        system = self.system.build()
        notification_report = await notification_service_v1.report()
        strategies = await strategy_builder_service_v1.list()

        panels = [
            self.panels.system_panel(system.uptime_seconds, len(system.modules)),
            self.panels.portfolio_panel(),
            self.panels.risk_panel(),
            self.panels.notification_panel(sent=notification_report.sent, failed=notification_report.failed),
        ]

        strategy_items = [
            DashboardStrategyItem(
                strategy_id=s.strategy_id,
                name=s.name,
                status=s.status,
                version=s.version,
                last_score=0,
            )
            for s in strategies
        ]

        return DashboardSnapshot(
            system=system,
            panels=panels,
            watchlist=self.watchlist.build_default(),
            strategies=strategy_items,
            signals=[
                DashboardSignalItem(symbol="BTC/USDT", direction="wait", confidence=0, reason="No active signal in dashboard snapshot.")
            ],
        )
