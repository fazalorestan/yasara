from dataclasses import dataclass, field
from typing import Any
from app.platform_core.clock import utc_now_iso

@dataclass
class BrokerOrderRequest:
    symbol: str
    side: str
    order_type: str
    quantity: float
    price: float | None = None
    reduce_only: bool = False
    client_order_id: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class BrokerOrderResult:
    accepted: bool
    order_id: str | None = None
    status: str = "blocked"
    reason: str = "execution_disabled"
    execution_allowed: bool = False
    created_at: str = field(default_factory=utc_now_iso)

@dataclass
class BrokerPosition:
    symbol: str
    side: str
    quantity: float
    entry_price: float
    unrealized_pnl: float = 0.0
    leverage: float = 1.0

@dataclass
class BrokerWalletBalance:
    asset: str
    total: float
    available: float
    locked: float = 0.0
