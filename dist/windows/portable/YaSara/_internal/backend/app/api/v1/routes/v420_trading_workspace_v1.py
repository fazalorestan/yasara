from fastapi import APIRouter
from app.v420_trading_workspace.models import TradingWorkspaceSummaryV420

router = APIRouter(prefix="/v4-20/trading-workspace", tags=["v4.20-trading-workspace"])

@router.get("/summary")
async def summary():
    return TradingWorkspaceSummaryV420()
