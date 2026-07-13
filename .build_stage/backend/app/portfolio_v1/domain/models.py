from datetime import datetime, timezone
from enum import StrEnum
from pydantic import BaseModel, Field
from app.decision_v1.domain.models import DecisionDirection

class AssetClass(StrEnum):
    CRYPTO = "crypto"
    STABLECOIN = "stablecoin"
    CASH = "cash"

class PositionStatus(StrEnum):
    OPEN = "open"
    CLOSED = "closed"

class PortfolioPosition(BaseModel):
    symbol: str
    direction: DecisionDirection
    quantity: float
    entry_price: float
    mark_price: float
    leverage: float = 1.0
    margin: float = 0
    asset_class: AssetClass = AssetClass.CRYPTO
    status: PositionStatus = PositionStatus.OPEN
    opened_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @property
    def notional(self) -> float:
        return abs(self.quantity * self.mark_price)

    @property
    def unrealized_pnl(self) -> float:
        if self.direction == DecisionDirection.LONG:
            return (self.mark_price - self.entry_price) * self.quantity
        if self.direction == DecisionDirection.SHORT:
            return (self.entry_price - self.mark_price) * self.quantity
        return 0

class PortfolioSnapshot(BaseModel):
    account_id: str = "default"
    equity: float
    cash: float = 0
    positions: list[PortfolioPosition] = Field(default_factory=list)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class ExposureItem(BaseModel):
    symbol: str
    notional: float
    exposure_pct: float
    direction: DecisionDirection
    pnl: float

class ExposureMatrix(BaseModel):
    total_exposure: float
    total_exposure_pct: float
    long_exposure: float
    short_exposure: float
    net_exposure: float
    items: list[ExposureItem]

class CorrelationPair(BaseModel):
    symbol_a: str
    symbol_b: str
    correlation: float

class CorrelationMatrix(BaseModel):
    pairs: list[CorrelationPair]
    average_abs_correlation: float
    high_correlation_count: int

class AllocationItem(BaseModel):
    symbol: str
    current_pct: float
    target_pct: float
    rebalance_required: bool
    delta_pct: float

class AllocationReport(BaseModel):
    items: list[AllocationItem]
    concentration_score: float
    diversification_score: float

class PortfolioRiskReport(BaseModel):
    exposure_score: float
    concentration_score: float
    correlation_score: float
    drawdown_score: float
    final_risk_score: float
    warnings: list[str] = Field(default_factory=list)

class EquityCurvePoint(BaseModel):
    timestamp: datetime
    equity: float
    drawdown_pct: float = 0

class PortfolioAnalyticsReport(BaseModel):
    snapshot: PortfolioSnapshot
    exposure: ExposureMatrix
    correlations: CorrelationMatrix
    allocation: AllocationReport
    risk: PortfolioRiskReport
    equity_curve: list[EquityCurvePoint] = Field(default_factory=list)
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
