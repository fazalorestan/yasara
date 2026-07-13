from pydantic import BaseModel, Field


class BacktestBenchmarkSummaryV44(BaseModel):
    ready: bool = True
    phase: str = "v4_4_backtest_benchmark_engine_foundation"
    product_progress_percent: int = 94
    remaining_to_professional_product_percent: int = 6
    constitution_version: str = "YASARA_MASTER_REQUIREMENTS_FINAL_V4"
    constitution_compliant: bool = True
    safety: str = "backtest_only_no_real_execution"


class BacktestRequestV44(BaseModel):
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    timeframe: str = "1m"
    initial_equity: float = 10000
    risk_per_trade_percent: float = 1.0
    fee_percent: float = 0.04
    limit: int = 200
    strategy_name: str = "multilayer_signal_v4_2"
    version: str = "v4.4"


class BenchmarkRequestV44(BaseModel):
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    timeframe: str = "1m"
    versions: list[str] = Field(default_factory=lambda: ["v4.2", "v4.3", "v4.4"])
