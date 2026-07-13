from enum import Enum
from pydantic import BaseModel, Field
from time import time


class RiskDecisionV11(str, Enum):
    ALLOW = "allow"
    BLOCK = "block"
    WARN = "warn"


class RiskViolationTypeV11(str, Enum):
    ORDER_SIZE = "order_size"
    POSITION_SIZE = "position_size"
    DAILY_LOSS = "daily_loss"
    LIVE_TRADING = "live_trading"
    INVALID_PRICE = "invalid_price"


class RiskRuleV11(BaseModel):
    key: str
    enabled: bool = True
    threshold: float | None = None
    message: str = ""


class RiskViolationV11(BaseModel):
    violation_type: RiskViolationTypeV11
    message: str
    value: float | None = None
    threshold: float | None = None


class RiskCheckResultV11(BaseModel):
    decision: RiskDecisionV11
    allowed: bool
    violations: list[RiskViolationV11] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    timestamp: float = Field(default_factory=time)


class RiskConfigV11(BaseModel):
    max_order_notional: float = 1000.0
    max_position_notional: float = 2500.0
    max_daily_loss: float = 250.0
    live_trading_enabled: bool = False
