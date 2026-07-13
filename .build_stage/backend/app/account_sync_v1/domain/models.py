from datetime import datetime, timezone, timedelta
from enum import StrEnum
from pydantic import BaseModel, Field
from app.exchange_private_v1.domain.models import PrivateExchange

class SyncStatus(StrEnum):
    IDLE = "idle"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"

class StreamConnectionStatus(StrEnum):
    DISCONNECTED = "disconnected"
    CONNECTED = "connected"
    RECONNECTING = "reconnecting"
    FAILED = "failed"

class AccountEventType(StrEnum):
    BALANCE_UPDATE = "balance_update"
    POSITION_UPDATE = "position_update"
    ORDER_UPDATE = "order_update"
    ACCOUNT_CONFIG_UPDATE = "account_config_update"
    UNKNOWN = "unknown"

class ListenKeyRecord(BaseModel):
    owner_id: str = "default"
    exchange: PrivateExchange = PrivateExchange.BINANCE_FUTURES
    listen_key: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    expires_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc) + timedelta(minutes=55))
    keepalive_count: int = 0
    dry_run: bool = True

    @property
    def expired(self) -> bool:
        return datetime.now(timezone.utc) >= self.expires_at

class AccountSyncSnapshot(BaseModel):
    owner_id: str = "default"
    exchange: PrivateExchange = PrivateExchange.BINANCE_FUTURES
    balances: dict[str, float] = Field(default_factory=dict)
    positions: list[dict] = Field(default_factory=list)
    open_orders: list[dict] = Field(default_factory=list)
    status: SyncStatus = SyncStatus.IDLE
    last_error: str = ""
    synced_at: datetime | None = None

class AccountStreamEvent(BaseModel):
    event_id: str
    owner_id: str = "default"
    exchange: PrivateExchange = PrivateExchange.BINANCE_FUTURES
    event_type: AccountEventType
    payload: dict = Field(default_factory=dict)
    received_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class StreamState(BaseModel):
    owner_id: str = "default"
    exchange: PrivateExchange = PrivateExchange.BINANCE_FUTURES
    status: StreamConnectionStatus = StreamConnectionStatus.DISCONNECTED
    listen_key: str | None = None
    events_received: int = 0
    reconnect_count: int = 0
    last_error: str = ""
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class OrderRecoveryReport(BaseModel):
    owner_id: str = "default"
    exchange: PrivateExchange = PrivateExchange.BINANCE_FUTURES
    recovered_orders: list[dict] = Field(default_factory=list)
    missing_orders: list[dict] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
