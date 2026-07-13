from datetime import datetime, timezone
from enum import StrEnum
from pydantic import BaseModel, Field
from app.decision_v1.domain.models import DecisionDirection

class PaperOrderSide(StrEnum):
    BUY = "buy"
    SELL = "sell"

class PaperOrderType(StrEnum):
    MARKET = "market"
    LIMIT = "limit"

class PaperOrderStatus(StrEnum):
    NEW = "new"
    FILLED = "filled"
    PARTIALLY_FILLED = "partially_filled"
    CANCELLED = "cancelled"
    REJECTED = "rejected"

class PaperPositionStatus(StrEnum):
    OPEN = "open"
    CLOSED = "closed"

class PaperExecutionMode(StrEnum):
    DRY_RUN = "dry_run"
    PAPER = "paper"

class PaperAccount(BaseModel):
    account_id: str = "paper-default"
    equity: float = 10000
    cash: float = 10000
    realized_pnl: float = 0
    unrealized_pnl: float = 0
    fees_paid: float = 0
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class PaperOrderRequest(BaseModel):
    symbol: str
    side: PaperOrderSide
    order_type: PaperOrderType = PaperOrderType.MARKET
    quantity: float
    price: float | None = None
    stop_loss: float | None = None
    take_profit: float | None = None
    client_order_id: str | None = None

class PaperOrder(BaseModel):
    order_id: str
    request: PaperOrderRequest
    status: PaperOrderStatus = PaperOrderStatus.NEW
    filled_quantity: float = 0
    average_fill_price: float | None = None
    fee: float = 0
    rejection_reason: str = ""
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    filled_at: datetime | None = None

class PaperPosition(BaseModel):
    position_id: str
    symbol: str
    direction: DecisionDirection
    quantity: float
    entry_price: float
    mark_price: float
    stop_loss: float | None = None
    take_profit: float | None = None
    trailing_stop_distance: float | None = None
    break_even_trigger_pct: float | None = None
    status: PaperPositionStatus = PaperPositionStatus.OPEN
    opened_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    closed_at: datetime | None = None
    realized_pnl: float = 0
    unrealized_pnl: float = 0
    exit_price: float | None = None
    exit_reason: str = ""

class PaperTradeJournalEntry(BaseModel):
    entry_id: str
    account_id: str
    symbol: str
    action: str
    message: str
    pnl: float = 0
    metadata: dict = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class PaperTradingState(BaseModel):
    account: PaperAccount
    orders: list[PaperOrder] = Field(default_factory=list)
    positions: list[PaperPosition] = Field(default_factory=list)
    journal: list[PaperTradeJournalEntry] = Field(default_factory=list)

class PaperExecutionReport(BaseModel):
    accepted: bool
    order: PaperOrder | None = None
    position: PaperPosition | None = None
    message: str
    state: PaperTradingState | None = None

class PaperDashboard(BaseModel):
    equity: float
    cash: float
    realized_pnl: float
    unrealized_pnl: float
    open_positions: int
    total_orders: int
    fees_paid: float
    exposure: float
    journal_count: int
