from enum import Enum
from pydantic import BaseModel, Field
from typing import Any
from time import time


class ConnectionStateV11(str, Enum):
    CONNECTED = "connected"
    DISCONNECTED = "disconnected"
    RECONNECTING = "reconnecting"
    DEGRADED = "degraded"


class MarketEventTypeV11(str, Enum):
    TICKER_UPDATED = "ticker_updated"
    ORDER_BOOK_UPDATED = "order_book_updated"
    TRADE_UPDATED = "trade_updated"
    FUNDING_UPDATED = "funding_updated"
    SNAPSHOT_UPDATED = "snapshot_updated"


class MarketTickerV11(BaseModel):
    exchange: str
    symbol: str
    normalized_symbol: str
    last_price: float
    bid: float | None = None
    ask: float | None = None
    volume_24h: float | None = None
    timestamp: float = Field(default_factory=time)

    @property
    def spread(self) -> float | None:
        if self.bid is None or self.ask is None:
            return None
        return max(self.ask - self.bid, 0.0)


class MarketSnapshotItemV11(BaseModel):
    exchange: str
    symbol: str
    normalized_symbol: str
    last_price: float | None = None
    bid: float | None = None
    ask: float | None = None
    spread: float | None = None
    volume_24h: float | None = None
    funding_rate: float | None = None
    open_interest: float | None = None
    timestamp: float = Field(default_factory=time)


class MarketSnapshotV11(BaseModel):
    ready: bool
    count: int
    items: list[MarketSnapshotItemV11] = Field(default_factory=list)


class MarketEventV11(BaseModel):
    event_type: MarketEventTypeV11
    exchange: str
    symbol: str
    payload: dict[str, Any] = Field(default_factory=dict)
    timestamp: float = Field(default_factory=time)


class SubscriptionRequestV11(BaseModel):
    exchange: str
    symbols: list[str]
    channels: list[str] = Field(default_factory=lambda: ["ticker"])


class ExchangeHealthV11(BaseModel):
    exchange: str
    state: ConnectionStateV11
    last_heartbeat: float | None = None
    reconnect_attempts: int = 0
    message: str = ""


class RateLimitRuleV11(BaseModel):
    exchange: str
    max_requests: int
    per_seconds: int
