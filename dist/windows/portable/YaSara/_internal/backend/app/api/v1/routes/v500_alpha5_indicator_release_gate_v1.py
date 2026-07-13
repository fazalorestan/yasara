from fastapi import APIRouter
from app.v500_alpha5_indicator_release_gate.service import IndicatorReleaseGateFacadeV500Alpha5

router = APIRouter(prefix="/v5-0-alpha-5/indicator-release-gate", tags=["v5.0-alpha.5-indicator-release-gate"])
_service = IndicatorReleaseGateFacadeV500Alpha5()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/gate")
async def gate():
    return _service.gate()

@router.get("/stability")
async def stability():
    return _service.stability()

@router.get("/regression")
async def regression():
    return _service.regression()

@router.get("/checkpoint")
async def checkpoint():
    return _service.checkpoint()

@router.get("/rc-contract")
async def rc_contract():
    return _service.rc_contract()

@router.get("/full-report")
async def full_report():
    return _service.full_report()
