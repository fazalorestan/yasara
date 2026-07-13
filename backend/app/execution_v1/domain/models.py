from datetime import datetime, timezone
from enum import StrEnum
from pydantic import BaseModel, Field
from app.decision_v1.domain.models import DecisionDirection

class ExecutionMode(StrEnum):
    DRY_RUN = "dry_run"
    PAPER = "paper"
    LIVE_DISABLED = "live_disabled"

class ExecutionIntentStatus(StrEnum):
    CREATED = "created"
    APPROVED = "approved"
    REJECTED = "rejected"
    EXECUTED = "executed"
    FAILED = "failed"

class ExecutionOrderType(StrEnum):
    MARKET = "market"
    LIMIT = "limit"

class ExecutionSide(StrEnum):
    BUY = "buy"
    SELL = "sell"

class ExecutionIntent(BaseModel):
    symbol: str
    direction: DecisionDirection
    side: ExecutionSide
    order_type: ExecutionOrderType = ExecutionOrderType.MARKET
    quantity: float
    price: float | None = None
    stop_loss: float | None = None
    take_profit: float | None = None
    mode: ExecutionMode = ExecutionMode.DRY_RUN
    source: str = "manual"
    metadata: dict = Field(default_factory=dict)

class SafetyGateResult(BaseModel):
    passed: bool
    reasons: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)

class ExecutionResult(BaseModel):
    execution_id: str
    intent: ExecutionIntent
    status: ExecutionIntentStatus
    safety: SafetyGateResult
    exchange_order_id: str | None = None
    filled_quantity: float = 0
    average_price: float | None = None
    message: str = ""
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class ExecutionAuditEntry(BaseModel):
    audit_id: str
    event: str
    message: str
    intent: ExecutionIntent | None = None
    result: ExecutionResult | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
