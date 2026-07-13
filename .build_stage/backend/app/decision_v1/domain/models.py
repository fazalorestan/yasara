from datetime import datetime, timedelta, timezone
from enum import StrEnum
from typing import Any
from pydantic import BaseModel, Field

class DecisionDirection(StrEnum):
    LONG = "long"
    SHORT = "short"
    WAIT = "wait"
    NO_TRADE = "no_trade"

class DecisionClass(StrEnum):
    STRONG_BUY = "strong_buy"
    BUY = "buy"
    WEAK_BUY = "weak_buy"
    NEUTRAL = "neutral"
    WEAK_SELL = "weak_sell"
    SELL = "sell"
    STRONG_SELL = "strong_sell"
    NO_TRADE = "no_trade"

class RuleStatus(StrEnum):
    PASSED = "passed"
    WARNING = "warning"
    FAILED = "failed"
    DISABLED = "disabled"

class StrategyCode(StrEnum):
    TREND = "trend"
    BREAKOUT = "breakout"
    MOMENTUM = "momentum"
    MEAN_REVERSION = "mean_reversion"
    COMPOSITE = "composite"

class ConfidenceBreakdown(BaseModel):
    trend: float = 0
    rsi: float = 0
    macd: float = 0
    structure: float = 0
    volume: float = 0
    volatility: float = 0
    multi_timeframe: float = 0
    regime: float = 0

class DecisionWeights(BaseModel):
    trend: float = 0.20
    rsi: float = 0.08
    macd: float = 0.10
    structure: float = 0.20
    volume: float = 0.10
    volatility: float = 0.10
    multi_timeframe: float = 0.15
    regime: float = 0.07

    def normalized(self) -> dict[str, float]:
        data = self.model_dump()
        total = sum(max(0, v) for v in data.values()) or 1.0
        return {k: max(0, v) / total for k, v in data.items()}

class RuleResult(BaseModel):
    name: str
    status: RuleStatus
    score_adjustment: float = 0
    reason: str = ""
    metadata: dict[str, Any] = Field(default_factory=dict)

class StrategyResult(BaseModel):
    strategy: StrategyCode
    direction: DecisionDirection
    confidence: float
    quality: float
    reasons: list[str] = Field(default_factory=list)

class DecisionScores(BaseModel):
    confidence: float = 0
    probability: float = 0
    quality: float = 0
    reliability: float = 0
    risk: float = 0
    reward: float = 0

class SignalPlan(BaseModel):
    entry_zone_low: float | None = None
    entry_zone_high: float | None = None
    stop_loss: float | None = None
    tp1: float | None = None
    tp2: float | None = None
    tp3: float | None = None
    invalidation: str = ""
    lifetime_minutes: int = 60

class DecisionExplanation(BaseModel):
    summary: str
    reasons: list[str] = Field(default_factory=list)
    confirmations: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    failed_rules: list[str] = Field(default_factory=list)

class DecisionObject(BaseModel):
    exchange: str
    symbol: str
    direction: DecisionDirection
    decision_class: DecisionClass
    scores: DecisionScores
    confidence_breakdown: ConfidenceBreakdown
    weights: DecisionWeights
    signal: SignalPlan
    rules: list[RuleResult] = Field(default_factory=list)
    strategies: list[StrategyResult] = Field(default_factory=list)
    explanation: DecisionExplanation
    rank_score: float = 0
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    expires_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc) + timedelta(minutes=60))
    source: dict[str, Any] = Field(default_factory=dict)

class RankedDecision(BaseModel):
    rank: int
    decision: DecisionObject

class DecisionBatch(BaseModel):
    decisions: list[RankedDecision]
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
