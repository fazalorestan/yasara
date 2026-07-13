from pydantic import BaseModel

class StrategyCoreSummaryV500Alpha41(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_41_strategy_engine_package_a"
    scope: str = "strategy_core_contract_layer"
    strategy_registry: bool = True
    strategy_contract: bool = True
    signal_contract: bool = True
    rule_contract: bool = True
    strategy_safety_policy: bool = True
    real_execution_enabled: bool = False
    auto_trading_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 60
