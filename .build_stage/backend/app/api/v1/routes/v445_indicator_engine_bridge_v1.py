from fastapi import APIRouter
from app.v445_indicator_engine_bridge.service import IndicatorEngineBridgeFacadeV445

router = APIRouter(prefix="/v4-45/indicator-engine-bridge", tags=["v4.45-indicator-engine-bridge"])
_service = IndicatorEngineBridgeFacadeV445()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/bridge-sample")
async def bridge_sample():
    return _service.bridge_sample()

@router.get("/bridge-contract")
async def bridge_contract():
    return _service.bridge_contract()
