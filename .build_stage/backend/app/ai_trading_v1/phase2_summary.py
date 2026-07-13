from pydantic import BaseModel, Field

class AITradingPhaseSummaryV1(BaseModel):
    phase: str = "ai_trading_phase_2"
    modules: list[str] = Field(default_factory=list)
    ready: bool = True

class AITradingPhaseSummaryBuilderV1:
    def build(self) -> AITradingPhaseSummaryV1:
        return AITradingPhaseSummaryV1(modules=[
            "signal_fusion",
            "risk_manager",
            "position_sizer",
            "portfolio_optimizer",
            "trade_explainer",
            "scenario_simulator",
            "confidence_engine",
            "market_context",
            "recommendation",
        ])
