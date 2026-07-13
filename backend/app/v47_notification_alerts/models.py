from pydantic import BaseModel, Field
from typing import Literal


class NotificationAlertSummaryV47(BaseModel):
    ready: bool = True
    phase: str = "v4_7_notification_alert_engine_foundation"
    product_progress_percent: int = 98
    remaining_to_professional_product_percent: int = 2
    constitution_version: str = "YASARA_MASTER_REQUIREMENTS_FINAL_V4"
    constitution_compliant: bool = True
    safety: str = "notification_only_no_real_execution"


class AlertRuleV47(BaseModel):
    id: str
    name: str
    enabled: bool = True
    source: Literal["signal", "risk", "journal", "system"] = "signal"
    condition: str = "confidence_gte"
    threshold: float = 70
    channels: list[str] = Field(default_factory=lambda: ["desktop"])
    severity: Literal["info", "warning", "critical"] = "info"


class AlertEventV47(BaseModel):
    id: str
    title: str
    message: str
    severity: Literal["info", "warning", "critical"] = "info"
    source: str = "system"
    channels: list[str] = Field(default_factory=lambda: ["desktop"])
    status: str = "created"
    created_at: str = "auto"


class SignalAlertRequestV47(BaseModel):
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    timeframe: str = "1m"
    min_confidence: float = 60
