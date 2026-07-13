from datetime import datetime, timezone
from enum import StrEnum
from typing import Any
from pydantic import BaseModel, Field

class ExchangeCode(StrEnum):
    BINANCE_FUTURES = "binance_futures"
    BITUNIX_FUTURES = "bitunix_futures"

class SymbolStatus(StrEnum):
    TRADING = "trading"
    HALTED = "halted"
    UNKNOWN = "unknown"

class Timeframe(StrEnum):
    M1 = "1m"
    M3 = "3m"
    M5 = "5m"
    M15 = "15m"
    M30 = "30m"
    H1 = "1h"
    H2 = "2h"
    H4 = "4h"
    H6 = "6h"
    H8 = "8h"
    H12 = "12h"
    D1 = "1d"
    W1 = "1w"
    MN1 = "1M"

class MarketSymbol(BaseModel):
    exchange: ExchangeCode
    symbol: str
    base_asset: str
    quote_asset: str
    status: SymbolStatus
    price_precision: int
    quantity_precision: int
    tick_size: float
    step_size: float
    min_quantity: float
    min_notional: float = 0
    raw: dict[str, Any] = Field(default_factory=dict)

class Candle(BaseModel):
    exchange: ExchangeCode
    symbol: str
    timeframe: Timeframe | str
    open_time: datetime
    close_time: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float
    quote_volume: float = 0
    trades: int = 0
    is_closed: bool = True

class Ticker(BaseModel):
    exchange: ExchangeCode
    symbol: str
    last_price: float
    bid_price: float | None = None
    ask_price: float | None = None
    high_24h: float | None = None
    low_24h: float | None = None
    volume_24h: float | None = None
    quote_volume_24h: float | None = None
    price_change_percent_24h: float | None = None
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class OrderBookLevel(BaseModel):
    price: float
    quantity: float

class OrderBook(BaseModel):
    exchange: ExchangeCode
    symbol: str
    bids: list[OrderBookLevel]
    asks: list[OrderBookLevel]
    last_update_id: int | str | None = None
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class FundingRate(BaseModel):
    exchange: ExchangeCode
    symbol: str
    funding_rate: float
    funding_time: datetime | None = None
    next_funding_time: datetime | None = None
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class OpenInterest(BaseModel):
    exchange: ExchangeCode
    symbol: str
    open_interest: float
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class ExchangeHealth(BaseModel):
    exchange: ExchangeCode
    rest_available: bool
    websocket_available: bool = False
    latency_ms: float | None = None
    server_time: datetime | None = None
    clock_drift_ms: float | None = None
    message: str = ""
    checked_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
