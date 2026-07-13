from dataclasses import dataclass, field
from typing import Any
from app.platform_core.clock import utc_now_iso

@dataclass
class ExchangeInfo:
    exchange_id: str
    name: str
    exchange_type: str = "crypto"
    region: str = "global"
    enabled: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class ExchangeCapability:
    spot: bool = True
    futures: bool = False
    margin: bool = False
    options: bool = False
    rest: bool = True
    websocket: bool = False
    orderbook: bool = True
    trades: bool = True
    ohlcv: bool = True
    ticker: bool = True
    sandbox: bool = False
    testnet: bool = False
    iran_market: bool = False

@dataclass
class ExchangeMetadata:
    exchange_id: str
    timezone: str = "UTC"
    base_url: str = ""
    websocket_url: str = ""
    api_version: str = "v1"
    auth_type: str = "api_key"
    rate_limit_per_minute: int = 1200
    country: str = "global"

@dataclass
class ExchangeHealth:
    exchange_id: str
    status: str = "disconnected"
    latency_ms: int | None = None
    reconnect_count: int = 0
    last_ping_at: str = field(default_factory=utc_now_iso)
    maintenance: bool = False
    rate_limited: bool = False
