from fastapi import APIRouter
from app.v500_alpha8_signal_logic_expansion.service import SignalLogicExpansionFacadeV500Alpha8

router = APIRouter(prefix="/v5-0-alpha-8/signal-logic-expansion", tags=["v5.0-alpha.8-signal-logic-expansion"])
_service = SignalLogicExpansionFacadeV500Alpha8()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/evaluate-sample")
async def evaluate_sample(trend: str = "up"):
    return _service.evaluate_sample(trend)

@router.get("/safety")
async def safety():
    return _service.safety()

@router.get("/contract")
async def contract():
    return _service.contract()
