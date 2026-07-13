from pydantic import BaseModel, Field
from app.v11_paper_trading.service import PaperTradingServiceV11


class V11Phase6Summary(BaseModel):
    ready: bool
    phase: str = "v1_1_phase_6_paper_trading_engine"
    capabilities: list[str] = Field(default_factory=list)
    safety: str = "paper_trading_only_no_live_orders"


class V11Phase6SummaryBuilder:
    def build(self) -> V11Phase6Summary:
        snapshot = PaperTradingServiceV11().demo()
        return V11Phase6Summary(
            ready=snapshot.ready and snapshot.account.live_trading_enabled is False and len(snapshot.orders) >= 2,
            capabilities=[
                "paper_order_model",
                "paper_safety_guard",
                "paper_fill_engine",
                "paper_order_manager",
                "paper_position_manager",
                "paper_accounting",
                "paper_snapshot_api",
            ],
        )
