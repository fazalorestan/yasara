from fastapi import APIRouter
from app.v444_indicator_pine_source.service import IndicatorPineSourceServiceV444

router = APIRouter(prefix="/v4-44/indicator-pine-source", tags=["v4.44-indicator-pine-source"])
_service = IndicatorPineSourceServiceV444()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/archive")
async def archive():
    return _service.archive()

@router.get("/mapping")
async def mapping():
    return _service.mapping()

@router.get("/update-contract")
async def update_contract():
    return _service.update_contract()

@router.get("/source-status")
async def source_status():
    return _service.source_status()
