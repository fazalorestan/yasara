from datetime import datetime, timezone
from enum import StrEnum
from pydantic import BaseModel, Field

class TrendDirection(StrEnum):
    BULLISH = "bullish"
    BEARISH = "bearish"
    SIDEWAYS = "sideways"
    UNKNOWN = "unknown"

class MarketRegime(StrEnum):
    TRENDING = "trending"
    RANGING = "ranging"
    HIGH_VOLATILITY = "high_volatility"
    LOW_VOLATILITY = "low_volatility"
    UNKNOWN = "unknown"

class ScoreSet(BaseModel):
    confidence: float = 0
    quality: float = 0
    reliability: float = 0

class IndicatorPack(BaseModel):
    sma_20: float | None = None
    sma_50: float | None = None
    ema_20: float | None = None
    rsi_14: float | None = None
    macd: float | None = None
    macd_signal: float | None = None
    macd_histogram: float | None = None
    atr_14: float | None = None
    volume_sma_20: float | None = None
    relative_volume: float | None = None

class MarketStructurePack(BaseModel):
    trend: TrendDirection = TrendDirection.UNKNOWN
    higher_high: bool = False
    higher_low: bool = False
    lower_high: bool = False
    lower_low: bool = False
    last_swing_high: float | None = None
    last_swing_low: float | None = None
    break_of_structure: bool = False

class TimeframeIntelligence(BaseModel):
    symbol: str
    timeframe: str
    candles: int
    indicators: IndicatorPack
    structure: MarketStructurePack
    regime: MarketRegime
    scores: ScoreSet
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class MarketIntelligenceReport(BaseModel):
    exchange: str
    symbol: str
    timeframes: dict[str, TimeframeIntelligence]
    overall_trend: TrendDirection
    overall_regime: MarketRegime
    confidence: float
    quality: float
    reliability: float
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
