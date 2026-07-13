from fastapi import APIRouter
from pydantic import BaseModel, Field
from app.dashboard_v1.application.service import dashboard_service_v1

router = APIRouter(prefix="/dashboard-v1", tags=["dashboard-v1"])

class WatchlistRequest(BaseModel):
    prices: dict[str, float] = Field(default_factory=dict)

@router.get("/snapshot")
async def dashboard_snapshot():
    return await dashboard_service_v1.snapshot()

@router.post("/watchlist")
async def dashboard_watchlist(payload: WatchlistRequest):
    return await dashboard_service_v1.watchlist(payload.prices)

@router.get("/status")
async def dashboard_status():
    snapshot = await dashboard_service_v1.snapshot()
    return snapshot.system
