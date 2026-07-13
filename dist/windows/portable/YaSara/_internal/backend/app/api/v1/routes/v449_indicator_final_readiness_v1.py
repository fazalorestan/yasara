from fastapi import APIRouter
from app.v449_indicator_final_readiness.service import IndicatorFinalReadinessFacadeV449

router = APIRouter(prefix="/v4-49/indicator-final-readiness", tags=["v4.49-indicator-final-readiness"])
_service = IndicatorFinalReadinessFacadeV449()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/gate")
async def gate():
    return _service.gate()

@router.get("/e2e-contract")
async def e2e_contract():
    return _service.e2e_contract()

@router.get("/safety")
async def safety():
    return _service.safety()

@router.get("/v5-readiness")
async def v5_readiness():
    return _service.v5_readiness()
