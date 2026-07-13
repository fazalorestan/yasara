from app.v11_dashboard_runtime.models import DashboardPanelV11
from app.v11_market_data.service import MarketDataServiceV11
from app.v11_exchange_connectivity.service import ExchangeConnectivityServiceV11
from app.v11_ai_market_intelligence.service import AIMarketIntelligenceServiceV11


class DashboardPanelBuilderV11:
    def market_panel(self) -> DashboardPanelV11:
        service = MarketDataServiceV11()
        service.bootstrap_demo()
        snapshot = service.engine.snapshot()
        return DashboardPanelV11(
            key="market_snapshot",
            title="Market Snapshot",
            payload=snapshot.model_dump(),
        )

    def exchange_panel(self) -> DashboardPanelV11:
        diagnostics = ExchangeConnectivityServiceV11().diagnostics()
        return DashboardPanelV11(
            key="exchange_connectivity",
            title="Exchange Connectivity",
            payload=diagnostics,
        )

    def ai_panel(self) -> DashboardPanelV11:
        payload = AIMarketIntelligenceServiceV11().dashboard_payload()
        return DashboardPanelV11(
            key="ai_market_intelligence",
            title="AI Market Intelligence",
            payload=payload,
        )

    def all_panels(self) -> list[DashboardPanelV11]:
        return [
            self.market_panel(),
            self.exchange_panel(),
            self.ai_panel(),
        ]
