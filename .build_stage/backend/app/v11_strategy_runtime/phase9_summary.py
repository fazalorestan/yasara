from pydantic import BaseModel, Field
from app.v11_strategy_runtime.service import StrategyRuntimeServiceV11


class V11Phase9Summary(BaseModel):
    ready: bool
    phase: str = "v1_1_phase_9_strategy_runtime_engine"
    capabilities: list[str] = Field(default_factory=list)
    safety: str = "strategy_signal_only_no_live_execution"


class V11Phase9SummaryBuilder:
    def build(self) -> V11Phase9Summary:
        snapshot = StrategyRuntimeServiceV11().snapshot()
        return V11Phase9Summary(
            ready=snapshot.ready and len(snapshot.rules) >= 1 and len(snapshot.signals) >= 1,
            capabilities=[
                "strategy_rule_model",
                "strategy_conditions",
                "strategy_rule_engine",
                "strategy_store",
                "strategy_context_builder",
                "strategy_signal_output",
                "strategy_runtime_api",
            ],
        )
