from datetime import datetime, timezone
from enum import StrEnum
from pydantic import BaseModel, Field
from app.decision_v1.domain.models import DecisionObject, DecisionDirection

class RiskProfile(StrEnum):
    CONSERVATIVE = "conservative"
    BALANCED = "balanced"
    AGGRESSIVE = "aggressive"

class RiskDecision(StrEnum):
    APPROVED = "approved"
    REDUCED = "reduced"
    REJECTED = "rejected"

class PositionSizingMethod(StrEnum):
    FIXED_FRACTIONAL = "fixed_fractional"
    ATR_BASED = "atr_based"
    CONFIDENCE_ADJUSTED = "confidence_adjusted"

class AccountSnapshot(BaseModel):
    equity: float
    balance: float | None = None
    free_margin: float | None = None
    daily_pnl: float = 0
    weekly_pnl: float = 0
    monthly_pnl: float = 0
    open_positions: int = 0
    current_exposure: float = 0
    consecutive_losses: int = 0

class RiskLimits(BaseModel):
    max_risk_per_trade_pct: float = 1.0
    max_daily_loss_pct: float = 3.0
    max_weekly_loss_pct: float = 7.0
    max_monthly_loss_pct: float = 12.0
    max_open_positions: int = 5
    max_total_exposure_pct: float = 30.0
    max_symbol_exposure_pct: float = 10.0
    max_leverage: float = 5.0
    min_risk_reward: float = 1.5
    max_consecutive_losses: int = 4

class ExistingExposure(BaseModel):
    symbol: str
    direction: DecisionDirection
    notional: float
    correlation_group: str = "crypto_major"

class PositionSize(BaseModel):
    method: PositionSizingMethod
    quantity: float
    notional: float
    risk_amount: float
    risk_pct: float
    leverage: float = 1.0
    margin_required: float = 0

class RiskRewardValidation(BaseModel):
    rr_tp1: float | None = None
    rr_tp2: float | None = None
    rr_tp3: float | None = None
    valid: bool = False
    reason: str = ""

class RiskRuleResult(BaseModel):
    name: str
    passed: bool
    severity: str = "info"
    reason: str = ""
    adjustment_factor: float = 1.0

class RiskAssessment(BaseModel):
    symbol: str
    risk_decision: RiskDecision
    approved: bool
    original_decision: DecisionObject
    adjusted_confidence: float
    adjusted_probability: float
    position_size: PositionSize
    risk_reward: RiskRewardValidation
    rules: list[RiskRuleResult] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    rejection_reasons: list[str] = Field(default_factory=list)
    final_risk_score: float = 0
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
