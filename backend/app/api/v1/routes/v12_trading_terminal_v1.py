from fastapi import APIRouter
from app.v12_trading_terminal.service import TradingTerminalServiceV12

router = APIRouter(prefix="/v1-2/trading-terminal", tags=["v1.2-trading-terminal"])

@router.get("/summary")
async def summary():
    return TradingTerminalServiceV12().summary()
