from datetime import datetime, timezone
from enum import StrEnum
from pydantic import BaseModel, Field

class PrivateExchange(StrEnum):
    BINANCE_FUTURES = "binance_futures"

class PrivateOrderSide(StrEnum):
    BUY = "BUY"
    SELL = "SELL"

class PrivateOrderType(StrEnum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"

class PrivateOrderStatus(StrEnum):
    ACCEPTED_DRY_RUN = "accepted_dry_run"
    REJECTED = "rejected"

class ExchangeCredentialRef(BaseModel):
    owner_id: str = "default"
    api_key_secret_name: str
    api_secret_secret_name: str
    exchange: PrivateExchange = PrivateExchange.BINANCE_FUTURES

class PrivateOrderRequest(BaseModel):
    symbol: str
    side: PrivateOrderSide
    order_type: PrivateOrderType = PrivateOrderType.MARKET
    quantity: float
    price: float | None = None
    reduce_only: bool = False
    dry_run: bool = True
    credential_ref: ExchangeCredentialRef | None = None
    metadata: dict = Field(default_factory=dict)

class PrivateOrderResult(BaseModel):
    accepted: bool
    status: PrivateOrderStatus
    exchange: PrivateExchange = PrivateExchange.BINANCE_FUTURES
    symbol: str
    side: PrivateOrderSide
    quantity: float
    exchange_order_id: str | None = None
    message: str
    signed_payload_preview: dict = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class ExchangeBalanceSnapshot(BaseModel):
    exchange: PrivateExchange
    owner_id: str
    balances: dict[str, float] = Field(default_factory=dict)
    dry_run: bool = True
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class ExchangePositionSnapshot(BaseModel):
    exchange: PrivateExchange
    owner_id: str
    positions: list[dict] = Field(default_factory=list)
    dry_run: bool = True
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
