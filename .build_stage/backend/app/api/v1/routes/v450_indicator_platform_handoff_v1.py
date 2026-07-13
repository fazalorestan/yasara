from fastapi import APIRouter
from app.v450_indicator_platform_handoff.service import IndicatorPlatformHandoffFacadeV450

router = APIRouter(prefix="/v4-50/indicator-platform-handoff", tags=["v4.50-indicator-platform-handoff"])
_service = IndicatorPlatformHandoffFacadeV450()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/handoff")
async def handoff():
    return _service.handoff()

@router.get("/release-manifest")
async def release_manifest():
    return _service.release_manifest()

@router.get("/v5-contract")
async def v5_contract():
    return _service.v5_contract()

@router.get("/compatibility")
async def compatibility():
    return _service.compatibility()

@router.get("/checklist")
async def checklist():
    return _service.checklist()
