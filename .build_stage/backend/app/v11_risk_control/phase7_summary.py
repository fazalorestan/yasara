from pydantic import BaseModel, Field
from app.v11_risk_control.service import RiskControlServiceV11


class V11Phase7Summary(BaseModel):
    ready: bool
    phase: str = "v1_1_phase_7_risk_control_position_guard"
    capabilities: list[str] = Field(default_factory=list)
    safety: str = "risk_guarded_paper_trading_only"


class V11Phase7SummaryBuilder:
    def build(self) -> V11Phase7Summary:
        status = RiskControlServiceV11().status()
        return V11Phase7Summary(
            ready=status["ready"] and status["live_trading_enabled"] is False,
            capabilities=[
                "risk_config",
                "order_notional_guard",
                "position_notional_guard",
                "daily_loss_guard",
                "live_trading_block",
                "guarded_paper_trading",
                "risk_control_api",
            ],
        )
