from datetime import datetime, timezone
from enum import StrEnum
from typing import Any
from pydantic import BaseModel, Field

class MarketEventType(StrEnum):
    KLINE = "kline"
    TICKER = "ticker"
    DEPTH = "depth"
    TRADE = "trade"
    FUNDING = "funding"
    HEALTH = "health"

class MarketEvent(BaseModel):
    event_type: MarketEventType
    exchange: str
    symbol: str
    payload: dict[str, Any]
    received_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
