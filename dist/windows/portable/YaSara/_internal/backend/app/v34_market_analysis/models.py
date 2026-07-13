from pydantic import BaseModel, Field


class MarketAnalysisSummaryV34(BaseModel):
    ready: bool = True
    phase: str = "v3_4_market_analysis_engine_core"
    product_progress_percent: int = 72
    remaining_to_professional_product_percent: int = 28
    constitution_compliant: bool = True
    safety: str = "analysis_only_live_trading_disabled"


class MarketAnalysisRequestV34(BaseModel):
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    timeframes: list[str] = Field(default_factory=lambda: ["1m", "5m", "15m", "1h", "4h"])
    limit: int = 120
    feature_flags: dict = Field(default_factory=lambda: {
        "multi_timeframe": True,
        "trend_detection": True,
        "range_detection": True,
        "volatility_detection": True,
        "market_regime": True,
        "session_analysis": True,
        "volume_analysis": True,
        "momentum_analysis": True,
    })
