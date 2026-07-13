from fastapi import APIRouter
from app.v12_market_workspace.service import MarketWorkspaceServiceV12

router = APIRouter(prefix="/v1-2/market-workspace", tags=["v1.2-market-workspace"])

@router.get("/summary")
async def summary():
    return MarketWorkspaceServiceV12().summary()
