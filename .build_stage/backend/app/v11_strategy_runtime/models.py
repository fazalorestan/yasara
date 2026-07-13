from enum import Enum
from pydantic import BaseModel, Field
from time import time
from uuid import uuid4


class StrategyActionV11(str, Enum):
    BUY = "buy"
    SELL = "sell"
    HOLD = "hold"
    BLOCK = "block"


class StrategyConditionTypeV11(str, Enum):
    PRICE_ABOVE = "price_above"
    PRICE_BELOW = "price_below"
    AI_SCORE_ABOVE = "ai_score_above"
    RISK_ALLOWED = "risk_allowed"


class StrategyConditionV11(BaseModel):
    condition_type: StrategyConditionTypeV11
    value: float | bool
    symbol: str | None = None


class StrategyRuleV11(BaseModel):
    rule_id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    conditions: list[StrategyConditionV11] = Field(default_factory=list)
    action: StrategyActionV11 = StrategyActionV11.HOLD
    enabled: bool = True


class StrategyContextV11(BaseModel):
    symbol: str
    price: float
    ai_score: float = 0.0
    risk_allowed: bool = True


class StrategySignalV11(BaseModel):
    symbol: str
    action: StrategyActionV11
    confidence: float
    matched_rules: list[str] = Field(default_factory=list)
    reason: str = ""
    timestamp: float = Field(default_factory=time)


class StrategyRuntimeSnapshotV11(BaseModel):
    ready: bool
    rules: list[StrategyRuleV11] = Field(default_factory=list)
    signals: list[StrategySignalV11] = Field(default_factory=list)
    safety: str = "strategy_signal_only_no_live_execution"
