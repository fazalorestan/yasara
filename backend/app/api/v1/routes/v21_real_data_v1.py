from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/v2-1/real-data", tags=["v2.1-real-data"])


class UserSettingsV21(BaseModel):
    theme: str = "dark"
    workspace: str = "market"
    default_exchange: str = "binance"
    default_symbol: str = "BTCUSDT"
    language: str = "en"
    live_trading_enabled: bool = False


class WatchlistItemV21(BaseModel):
    symbol: str
    normalized_symbol: str
    exchange: str = "binance"
    last_price: float = 0.0
    change_percent: float = 0.0
    favorite: bool = False


class WatchlistStateV21(BaseModel):
    ready: bool = True
    items: List[WatchlistItemV21] = []


class MarketSnapshotItem(BaseModel):
    symbol: str
    normalized_symbol: str
    exchange: str
    last_price: float = 0.0
    spread: float = 0.0
    favorite: bool = False
    source: str = "binance"


class OperationalMarketSnapshot(BaseModel):
    ready: bool = True
    exchange: str = "all"
    count: int = 0
    items: List[MarketSnapshotItem] = []


@router.get("/settings", response_model=UserSettingsV21)
async def settings() -> UserSettingsV21:
    return UserSettingsV21()


@router.get("/watchlist", response_model=WatchlistStateV21)
async def watchlist() -> WatchlistStateV21:
    return WatchlistStateV21()


@router.get("/market-snapshot", response_model=OperationalMarketSnapshot)
async def market_snapshot(exchange: str = "all") -> OperationalMarketSnapshot:
    return OperationalMarketSnapshot(exchange=exchange)
