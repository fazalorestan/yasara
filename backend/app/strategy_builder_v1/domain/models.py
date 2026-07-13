from datetime import datetime, timezone
from enum import StrEnum
from pydantic import BaseModel, Field

class StrategyStatus(StrEnum):
    DRAFT = "draft"
    ACTIVE = "active"
    ARCHIVED = "archived"

class StrategyDirection(StrEnum):
    LONG = "long"
    SHORT = "short"
    BOTH = "both"

class RuleOperator(StrEnum):
    GT = "gt"
    GTE = "gte"
    LT = "lt"
    LTE = "lte"
    EQ = "eq"
    NEQ = "neq"
    CROSSES_ABOVE = "crosses_above"
    CROSSES_BELOW = "crosses_below"

class RuleValueSource(StrEnum):
    INDICATOR = "indicator"
    MARKET_FIELD = "market_field"
    CONSTANT = "constant"
    ANALYSIS_FIELD = "analysis_field"

class RuleOperand(BaseModel):
    source: RuleValueSource
    key: str
    value: float | str | bool | None = None

class StrategyRule(BaseModel):
    rule_id: str
    left: RuleOperand
    operator: RuleOperator
    right: RuleOperand
    weight: float = 1.0
    required: bool = True
    description: str = ""

class RuleGroup(BaseModel):
    group_id: str
    name: str
    rules: list[StrategyRule] = Field(default_factory=list)
    min_score: float = 1.0

class StrategyDefinition(BaseModel):
    strategy_id: str
    name: str
    version: int = 1
    status: StrategyStatus = StrategyStatus.DRAFT
    direction: StrategyDirection = StrategyDirection.BOTH
    entry: RuleGroup
    exit: RuleGroup | None = None
    risk_filters: RuleGroup | None = None
    metadata: dict = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class StrategyValidationIssue(BaseModel):
    field: str
    message: str
    severity: str = "error"

class StrategyValidationResult(BaseModel):
    valid: bool
    issues: list[StrategyValidationIssue] = Field(default_factory=list)

class StrategyEvaluationContext(BaseModel):
    symbol: str
    timeframe: str = "1h"
    indicators: dict[str, float | int | bool | str] = Field(default_factory=dict)
    market_fields: dict[str, float | int | bool | str] = Field(default_factory=dict)
    analysis_fields: dict[str, float | int | bool | str] = Field(default_factory=dict)
    previous_indicators: dict[str, float | int | bool | str] = Field(default_factory=dict)
    previous_market_fields: dict[str, float | int | bool | str] = Field(default_factory=dict)

class RuleEvaluationResult(BaseModel):
    rule_id: str
    passed: bool
    score: float
    message: str

class StrategyEvaluationResult(BaseModel):
    strategy_id: str
    name: str
    symbol: str
    entry_passed: bool
    exit_passed: bool = False
    risk_passed: bool = True
    score: float
    confidence: float
    matched_rules: list[RuleEvaluationResult] = Field(default_factory=list)
    rejected_rules: list[RuleEvaluationResult] = Field(default_factory=list)
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
