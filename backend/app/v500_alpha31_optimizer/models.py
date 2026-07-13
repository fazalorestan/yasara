from pydantic import BaseModel
class OptimizerSummaryV500Alpha31(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_31_optimizer_foundation"
    scope: str = "optimizer_contracts"
    real_execution_enabled: bool = False
    auto_trading_enabled: bool = False
    backtest_link_enabled: bool = True
    backward_compatible: bool = True
    test_pack_size: int = 30
