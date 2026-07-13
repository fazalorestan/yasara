from datetime import datetime, timezone
from enum import StrEnum
from pydantic import BaseModel, Field

class AIInsightType(StrEnum):
    MARKET = "market"
    RISK = "risk"
    STRATEGY = "strategy"
    PORTFOLIO = "portfolio"
    SYSTEM = "system"

class AIInsightSeverity(StrEnum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"

class AIInsight(BaseModel):
    insight_id: str
    insight_type: AIInsightType
    title: str
    explanation: str
    severity: AIInsightSeverity = AIInsightSeverity.INFO
    confidence: float = 0
    recommended_actions: list[str] = Field(default_factory=list)
    evidence: dict = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class JournalEntryType(StrEnum):
    DECISION = "decision"
    TRADE = "trade"
    RISK_EVENT = "risk_event"
    SYSTEM_EVENT = "system_event"
    NOTE = "note"

class TradingJournalEntry(BaseModel):
    entry_id: str
    owner_id: str = "default"
    entry_type: JournalEntryType
    title: str
    body: str
    tags: list[str] = Field(default_factory=list)
    pnl: float = 0
    confidence: float = 0
    metadata: dict = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class JournalAnalytics(BaseModel):
    total_entries: int
    total_pnl: float
    average_confidence: float
    tags: dict[str, int] = Field(default_factory=dict)
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class ProductionMetric(BaseModel):
    key: str
    value: float | int | str | bool
    unit: str = ""
    labels: dict = Field(default_factory=dict)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class ProductionHealthReport(BaseModel):
    status: str
    metrics: list[ProductionMetric] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class SecurityChecklistItem(BaseModel):
    key: str
    title: str
    passed: bool
    severity: str = "medium"
    recommendation: str = ""

class SecurityChecklistReport(BaseModel):
    passed: bool
    items: list[SecurityChecklistItem] = Field(default_factory=list)
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
