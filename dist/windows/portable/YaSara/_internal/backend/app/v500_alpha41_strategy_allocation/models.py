from pydantic import BaseModel
class StrategyAllocationSummaryV500Alpha41(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_41_strategy_engine_package_c"
    scope: str = "strategy_portfolio_allocation_engine"
    portfolio_allocation: bool = True
    position_sizing: bool = True
    capital_allocation: bool = True
    exposure_controller: bool = True
    portfolio_balancer: bool = True
    allocation_safety_policy: bool = True
    real_execution_enabled: bool = False
    broker_connection_enabled: bool = False
    auto_trading_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 60
