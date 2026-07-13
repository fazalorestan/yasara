from datetime import datetime, timezone
from enum import StrEnum
from pydantic import BaseModel, Field

class NotificationChannel(StrEnum):
    TELEGRAM = "telegram"
    EMAIL = "email"
    DISCORD = "discord"
    WEBHOOK = "webhook"
    DESKTOP = "desktop"

class NotificationPriority(StrEnum):
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    CRITICAL = "critical"

class NotificationStatus(StrEnum):
    QUEUED = "queued"
    SENT = "sent"
    FAILED = "failed"
    RETRYING = "retrying"
    CANCELLED = "cancelled"

class NotificationType(StrEnum):
    SIGNAL = "signal"
    RISK = "risk"
    EXECUTION = "execution"
    SYSTEM = "system"
    HEALTH = "health"

class NotificationRecipient(BaseModel):
    channel: NotificationChannel
    target: str
    display_name: str | None = None
    enabled: bool = True

class NotificationMessage(BaseModel):
    notification_type: NotificationType
    title: str
    body: str
    priority: NotificationPriority = NotificationPriority.NORMAL
    metadata: dict = Field(default_factory=dict)

class NotificationDelivery(BaseModel):
    delivery_id: str
    recipient: NotificationRecipient
    message: NotificationMessage
    status: NotificationStatus = NotificationStatus.QUEUED
    attempts: int = 0
    max_attempts: int = 3
    last_error: str = ""
    provider_message_id: str | None = None
    queued_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    sent_at: datetime | None = None
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class NotificationBatch(BaseModel):
    deliveries: list[NotificationDelivery]
    queued: int
    skipped: int = 0

class DeliveryReport(BaseModel):
    total: int
    queued: int
    sent: int
    failed: int
    retrying: int
    cancelled: int
