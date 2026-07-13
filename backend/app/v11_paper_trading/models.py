from enum import Enum
from pydantic import BaseModel, Field
from time import time
from uuid import uuid4


class PaperOrderSideV11(str, Enum):
    BUY = "buy"
    SELL = "sell"


class PaperOrderTypeV11(str, Enum):
    MARKET = "market"
    LIMIT = "limit"


class PaperOrderStatusV11(str, Enum):
    NEW = "new"
    FILLED = "filled"
    REJECTED = "rejected"
    CANCELLED = "cancelled"


class PaperPositionSideV11(str, Enum):
    LONG = "long"
    SHORT = "short"
    FLAT = "flat"


class PaperOrderRequestV11(BaseModel):
    exchange: str
    symbol: str
    side: PaperOrderSideV11
    order_type: PaperOrderTypeV11 = PaperOrderTypeV11.MARKET
    quantity: float
    price: float | None = None


class PaperOrderV11(BaseModel):
    order_id: str = Field(default_factory=lambda: str(uuid4()))
    exchange: str
    symbol: str
    side: PaperOrderSideV11
    order_type: PaperOrderTypeV11
    quantity: float
    requested_price: float | None = None
    fill_price: float | None = None
    status: PaperOrderStatusV11 = PaperOrderStatusV11.NEW
    reason: str = ""
    timestamp: float = Field(default_factory=time)


class PaperPositionV11(BaseModel):
    exchange: str
    symbol: str
    side: PaperPositionSideV11 = PaperPositionSideV11.FLAT
    quantity: float = 0.0
    avg_price: float = 0.0
    realized_pnl: float = 0.0
    updated_at: float = Field(default_factory=time)


class PaperAccountV11(BaseModel):
    account_id: str = "default-paper"
    equity: float = 10000.0
    cash: float = 10000.0
    realized_pnl: float = 0.0
    live_trading_enabled: bool = False


class PaperTradingSnapshotV11(BaseModel):
    ready: bool
    account: PaperAccountV11
    orders: list[PaperOrderV11] = Field(default_factory=list)
    positions: list[PaperPositionV11] = Field(default_factory=list)
