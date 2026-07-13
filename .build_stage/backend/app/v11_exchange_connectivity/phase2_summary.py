from pydantic import BaseModel, Field
from app.v11_exchange_connectivity.service import ExchangeConnectivityServiceV11


class V11Phase2Summary(BaseModel):
    ready: bool
    phase: str = "v1_1_phase_2_exchange_connectivity_layer"
    capabilities: list[str] = Field(default_factory=list)
    safety: str = "read_only_connectivity_no_live_trading"


class V11Phase2SummaryBuilder:
    def build(self) -> V11Phase2Summary:
        summary = ExchangeConnectivityServiceV11().summary()
        return V11Phase2Summary(
            ready=summary.ready and summary.live_trading_enabled is False,
            capabilities=[
                "exchange_profiles",
                "read_only_rest_client",
                "safety_guard",
                "health_service",
                "failover_router",
                "rate_limit_profiles",
                "connectivity_router",
                "diagnostics_api",
            ],
        )
