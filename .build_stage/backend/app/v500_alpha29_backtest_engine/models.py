from pydantic import BaseModel
class BacktestEngineSummaryV500Alpha29(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_29_backtest_engine_foundation"
    scope: str = "backtest_engine_contracts"
    real_execution_enabled: bool = False
    auto_trading_enabled: bool = False
    real_market_data_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 20
