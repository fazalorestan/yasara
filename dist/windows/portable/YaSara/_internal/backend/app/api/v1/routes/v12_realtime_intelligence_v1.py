from fastapi import APIRouter
from app.v12_realtime_intelligence.service import RealtimeIntelligenceServiceV12
router = APIRouter(prefix="/v1-2/realtime-intelligence", tags=["v1.2-realtime-intelligence"])
@router.get("/summary")
async def summary():
    return RealtimeIntelligenceServiceV12().summary()
