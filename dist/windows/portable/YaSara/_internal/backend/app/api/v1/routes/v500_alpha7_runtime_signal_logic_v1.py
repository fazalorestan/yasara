from fastapi import APIRouter
from app.v500_alpha7_runtime_signal_logic.service import RuntimeSignalLogicFacadeV500Alpha7

router = APIRouter(prefix="/v5-0-alpha-7/runtime-signal-logic", tags=["v5.0-alpha.7-runtime-signal-logic"])
_service = RuntimeSignalLogicFacadeV500Alpha7()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/evaluate-sample")
async def evaluate_sample():
    return _service.evaluate_sample()

@router.get("/contract")
async def contract():
    return _service.contract()
