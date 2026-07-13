from pydantic import BaseModel

class StrategyScoringSummaryV500Alpha41(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_41_strategy_engine_package_b"
    scope: str = "strategy_signal_evaluation_scoring"
    signal_evaluator: bool = True
    strategy_score: bool = True
    confidence_model: bool = True
    rule_evaluator: bool = True
    signal_aggregator: bool = True
    scoring_safety_policy: bool = True
    real_execution_enabled: bool = False
    auto_trading_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 60
