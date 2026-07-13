from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/v4-5/paper-trading", tags=["v4.5-paper-trading"])


class PaperPosition(BaseModel):
    symbol: str
    side: str = "LONG"
    size: float = 0.0
    entry_price: float = 0.0
    pnl: float = 0.0
    pnl_percent: float = 0.0


class PaperTradingAccount(BaseModel):
    ready: bool = True
    mode: str = "paper"
    equity: float = 10000.0
    balance: float = 10000.0
    unrealized_pnl: float = 0.0
    unrealized_pnl_percent: float = 0.0
    open_positions: int = 0
    positions: List[PaperPosition] = []


class PaperTradingSummary(BaseModel):
    ready: bool = True
    mode: str = "paper"
    daily_pnl: float = 0.0
    total_return_percent: float = 0.0
    win_rate_percent: float = 0.0
    trades_today: int = 0


@router.get("/summary", response_model=PaperTradingSummary)
async def summary() -> PaperTradingSummary:
    return PaperTradingSummary()


@router.get("/account", response_model=PaperTradingAccount)
async def account() -> PaperTradingAccount:
    return PaperTradingAccount()
