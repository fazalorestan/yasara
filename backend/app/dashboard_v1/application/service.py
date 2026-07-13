from app.dashboard_v1.engine.snapshot_builder import DashboardSnapshotBuilderV1
from app.dashboard_v1.engine.watchlist import DashboardWatchlistEngineV1

class DashboardServiceV1:
    def __init__(self):
        self.snapshot_builder = DashboardSnapshotBuilderV1()
        self.watchlist_engine = DashboardWatchlistEngineV1()

    async def snapshot(self):
        return await self.snapshot_builder.build()

    async def watchlist(self, prices: dict[str, float] | None = None):
        if prices:
            return self.watchlist_engine.enrich(prices)
        return self.watchlist_engine.build_default()

dashboard_service_v1 = DashboardServiceV1()
