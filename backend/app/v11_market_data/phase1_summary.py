from pydantic import BaseModel, Field
from app.v11_market_data.service import MarketDataServiceV11


class V11Phase1Summary(BaseModel):
    ready: bool
    phase: str = "v1_1_phase_1_real_time_market_data_engine"
    capabilities: list[str] = Field(default_factory=list)
    safety: str = "read_only_market_data_no_live_trading"


class V11Phase1SummaryBuilder:
    def build(self) -> V11Phase1Summary:
        status = MarketDataServiceV11().bootstrap_demo()
        return V11Phase1Summary(
            ready=status["ready"] and status["snapshot_count"] >= 4,
            capabilities=[
                "websocket_manager",
                "rest_fallback",
                "market_cache",
                "symbol_registry",
                "subscription_manager",
                "health_monitor",
                "snapshot_api",
                "event_bus",
                "rate_limit_manager",
                "reconnect_policy",
            ],
        )
