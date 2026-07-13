from enum import Enum
from typing import Any
from pydantic import BaseModel, Field

class DecisionDirection(str, Enum):
    BUY = "BUY"
    SELL = "SELL"
    WAIT = "WAIT"

class EvidenceStatus(str, Enum):
    CONFIRMED = "confirmed"
    REJECTED = "rejected"
    UNAVAILABLE = "unavailable"

class EvidenceItem(BaseModel):
    source: str
    status: EvidenceStatus
    score: float | None = None
    reason: str | None = None
    payload: dict[str, Any] = Field(default_factory=dict)

class FusionRequest(BaseModel):
    symbol: str
    timeframe: str
    evidences: list[EvidenceItem] = Field(default_factory=list)
    risk_score: float | None = None
    portfolio_exposure: float | None = None

class DecisionResult(BaseModel):
    symbol: str
    timeframe: str
    decision: DecisionDirection
    confidence: float
    quality_score: float
    risk_score: float | None = None
    confirmations: list[EvidenceItem] = Field(default_factory=list)
    rejected: list[EvidenceItem] = Field(default_factory=list)
    explanation: list[str] = Field(default_factory=list)
    strategy_alignment: dict[str, float] = Field(default_factory=dict)
    source_count: int = 0
    real_data_only: bool = True
    mock_data: bool = False
    signal_only_default: bool = True
    auto_trading_enabled: bool = False
