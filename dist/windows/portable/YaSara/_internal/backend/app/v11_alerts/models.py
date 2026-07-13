from enum import Enum
from pydantic import BaseModel, Field
from time import time
from uuid import uuid4


class AlertSeverityV11(str, Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


class AlertSourceV11(str, Enum):
    MARKET = "market"
    AI = "ai"
    RISK = "risk"
    EXCHANGE = "exchange"
    SYSTEM = "system"


class AlertRuleTypeV11(str, Enum):
    PRICE_ABOVE = "price_above"
    PRICE_BELOW = "price_below"
    RISK_BLOCK = "risk_block"
    AI_SIGNAL = "ai_signal"
    EXCHANGE_DEGRADED = "exchange_degraded"


class AlertRuleV11(BaseModel):
    rule_id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    rule_type: AlertRuleTypeV11
    symbol: str | None = None
    threshold: float | None = None
    enabled: bool = True
    severity: AlertSeverityV11 = AlertSeverityV11.INFO


class AlertEventV11(BaseModel):
    alert_id: str = Field(default_factory=lambda: str(uuid4()))
    source: AlertSourceV11
    severity: AlertSeverityV11
    message: str
    symbol: str | None = None
    payload: dict = Field(default_factory=dict)
    timestamp: float = Field(default_factory=time)


class NotificationChannelV11(str, Enum):
    DASHBOARD = "dashboard"
    LOG = "log"
    WEBHOOK_STUB = "webhook_stub"


class NotificationDeliveryV11(BaseModel):
    channel: NotificationChannelV11
    delivered: bool
    message: str
    timestamp: float = Field(default_factory=time)


class AlertsSnapshotV11(BaseModel):
    ready: bool
    rules: list[AlertRuleV11] = Field(default_factory=list)
    events: list[AlertEventV11] = Field(default_factory=list)
    deliveries: list[NotificationDeliveryV11] = Field(default_factory=list)
