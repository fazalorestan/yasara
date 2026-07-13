from dataclasses import dataclass, field
from typing import Any
from app.platform_core.clock import utc_now_iso

@dataclass
class MarketSymbol:
    symbol: str
    base_asset: str
    quote_asset: str
    market_type: str = "crypto"
    exchange: str = "internal"
    enabled: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class OHLCV:
    symbol: str
    timeframe: str
    open_time: int
    open: float
    high: float
    low: float
    close: float
    volume: float
    exchange: str = "internal"

@dataclass
class OrderBookLevel:
    price: float
    quantity: float

@dataclass
class OrderBookSnapshot:
    symbol: str
    bids: list[OrderBookLevel] = field(default_factory=list)
    asks: list[OrderBookLevel] = field(default_factory=list)
    exchange: str = "internal"
    captured_at: str = field(default_factory=utc_now_iso)

@dataclass
class TradeTick:
    symbol: str
    price: float
    quantity: float
    side: str = "unknown"
    exchange: str = "internal"
    trade_time: str = field(default_factory=utc_now_iso)

@dataclass
class MarketSnapshot:
    symbol: str
    last_price: float
    change_24h: float = 0.0
    volume_24h: float = 0.0
    exchange: str = "internal"
    captured_at: str = field(default_factory=utc_now_iso)
