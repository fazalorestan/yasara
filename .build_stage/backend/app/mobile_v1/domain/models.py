from datetime import datetime, timezone
from enum import StrEnum
from pydantic import BaseModel, Field

class MobilePlatform(StrEnum):
    ANDROID = "android"
    IOS = "ios"
    UNKNOWN = "unknown"

class MobileTheme(StrEnum):
    SYSTEM = "system"
    LIGHT = "light"
    DARK = "dark"

class MobileNotificationLevel(StrEnum):
    ALL = "all"
    IMPORTANT = "important"
    CRITICAL = "critical"
    OFF = "off"

class MobileDevice(BaseModel):
    device_id: str
    owner_id: str = "default"
    platform: MobilePlatform = MobilePlatform.UNKNOWN
    push_token: str | None = None
    app_version: str = "1.0.0"
    enabled: bool = True
    registered_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    last_seen_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class MobileSettings(BaseModel):
    owner_id: str = "default"
    theme: MobileTheme = MobileTheme.SYSTEM
    notification_level: MobileNotificationLevel = MobileNotificationLevel.IMPORTANT
    biometric_enabled: bool = False
    offline_cache_enabled: bool = True
    default_timeframe: str = "1h"
    language: str = "fa"
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class MobilePortfolioSummary(BaseModel):
    equity: float = 10000
    cash: float = 10000
    exposure: float = 0
    realized_pnl: float = 0
    unrealized_pnl: float = 0
    open_positions: int = 0

class MobileSignalCard(BaseModel):
    symbol: str
    direction: str
    confidence: float
    risk_score: float = 0
    quality_score: float = 0
    title: str = ""
    summary: str = ""
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class MobileWatchlistCard(BaseModel):
    symbol: str
    price: float = 0
    change_percent: float = 0
    confidence: float = 0
    alert_enabled: bool = True

class MobileRiskCard(BaseModel):
    risk_score: float = 0
    risk_level: str = "low"
    max_daily_loss_reached: bool = False
    max_exposure_reached: bool = False
    warnings: list[str] = Field(default_factory=list)

class MobileHomePayload(BaseModel):
    owner_id: str = "default"
    portfolio: MobilePortfolioSummary
    watchlist: list[MobileWatchlistCard] = Field(default_factory=list)
    signals: list[MobileSignalCard] = Field(default_factory=list)
    risk: MobileRiskCard = Field(default_factory=MobileRiskCard)
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class MobileOfflineSyncPayload(BaseModel):
    owner_id: str = "default"
    settings: MobileSettings
    home: MobileHomePayload
    server_time: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    cache_ttl_seconds: int = 60

class MobilePushMessage(BaseModel):
    title: str
    body: str
    data: dict = Field(default_factory=dict)
    priority: str = "normal"

class MobilePushResult(BaseModel):
    accepted: bool
    dry_run: bool = True
    device_id: str
    provider_message_id: str | None = None
    message: str
