from datetime import datetime, timezone
from enum import StrEnum
from pydantic import BaseModel, Field

class SupportedExchange(StrEnum):
    BINANCE = "binance"
    BITUNIX = "bitunix"
    TOOBIT = "toobit"

class ExchangeCapability(StrEnum):
    MARKET_DATA = "market_data"
    OHLCV = "ohlcv"
    TICKER = "ticker"
    ORDER_BOOK = "order_book"
    PAPER_TRADING = "paper_trading"
    DRY_RUN_PRIVATE = "dry_run_private"
    LIVE_TRADING = "live_trading"

class ExchangeAdapterStatus(StrEnum):
    ACTIVE = "active"
    SCAFFOLD = "scaffold"
    DISABLED = "disabled"

class ExchangeDescriptor(BaseModel):
    exchange: SupportedExchange
    display_name: str
    status: ExchangeAdapterStatus
    base_url: str = ""
    futures_supported: bool = True
    spot_supported: bool = True
    capabilities: list[ExchangeCapability] = Field(default_factory=list)
    live_trading_enabled: bool = False
    notes: str = ""

class UnifiedTicker(BaseModel):
    exchange: SupportedExchange
    symbol: str
    price: float
    change_percent: float = 0
    volume: float = 0
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    raw: dict = Field(default_factory=dict)

class UnifiedKline(BaseModel):
    exchange: SupportedExchange
    symbol: str
    timeframe: str
    open_time: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    open: float
    high: float
    low: float
    close: float
    volume: float = 0
    raw: dict = Field(default_factory=dict)

class UnifiedOrderBook(BaseModel):
    exchange: SupportedExchange
    symbol: str
    bids: list[list[float]] = Field(default_factory=list)
    asks: list[list[float]] = Field(default_factory=list)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    raw: dict = Field(default_factory=dict)

class UnifiedPrivateOrderRequest(BaseModel):
    exchange: SupportedExchange
    symbol: str
    side: str
    order_type: str = "MARKET"
    quantity: float
    price: float | None = None
    dry_run: bool = True
    metadata: dict = Field(default_factory=dict)

class UnifiedPrivateOrderResult(BaseModel):
    accepted: bool
    exchange: SupportedExchange
    symbol: str
    side: str
    quantity: float
    dry_run: bool = True
    exchange_order_id: str | None = None
    message: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
