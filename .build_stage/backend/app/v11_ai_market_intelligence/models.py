from enum import Enum
from pydantic import BaseModel, Field
from time import time


class MarketRegimeV11(str, Enum):
    TRENDING_UP = "trending_up"
    TRENDING_DOWN = "trending_down"
    RANGING = "ranging"
    VOLATILE = "volatile"
    UNKNOWN = "unknown"


class SignalDirectionV11(str, Enum):
    LONG = "long"
    SHORT = "short"
    NEUTRAL = "neutral"


class RiskLevelV11(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class MarketFeatureVectorV11(BaseModel):
    symbol: str
    last_price: float
    volume_24h: float | None = None
    spread: float | None = None
    funding_rate: float | None = None
    open_interest: float | None = None
    volatility_score: float = 0.0
    momentum_score: float = 0.0


class RegimeAnalysisV11(BaseModel):
    symbol: str
    regime: MarketRegimeV11
    confidence: float
    reasons: list[str] = Field(default_factory=list)


class SignalScoreV11(BaseModel):
    symbol: str
    direction: SignalDirectionV11
    score: float
    confidence: float
    risk_level: RiskLevelV11
    explanation: str
    timestamp: float = Field(default_factory=time)


class AIMarketInsightV11(BaseModel):
    ready: bool
    symbol: str
    regime: RegimeAnalysisV11
    signal: SignalScoreV11
    warnings: list[str] = Field(default_factory=list)
