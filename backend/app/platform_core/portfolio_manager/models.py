from dataclasses import dataclass, field
from typing import Any
from app.platform_core.clock import utc_now_iso

@dataclass
class PortfolioHolding:
    symbol: str
    quantity: float
    average_price: float
    last_price: float
    asset_class: str = "crypto"
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class PortfolioSnapshot:
    account_id: str
    total_equity: float
    cash_balance: float
    holdings_value: float
    unrealized_pnl: float = 0.0
    captured_at: str = field(default_factory=utc_now_iso)

@dataclass
class AllocationItem:
    symbol: str
    value: float
    weight_pct: float

@dataclass
class EquityCurvePoint:
    timestamp: str
    equity: float

@dataclass
class PortfolioPnLSummary:
    realized_pnl: float = 0.0
    unrealized_pnl: float = 0.0
    total_pnl: float = 0.0
