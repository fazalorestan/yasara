from fastapi import APIRouter
from app.v500_alpha4_indicator_lifecycle.service import IndicatorLifecycleFacadeV500Alpha4

router = APIRouter(prefix="/v5-0-alpha-4/indicator-lifecycle", tags=["v5.0-alpha.4-indicator-lifecycle"])
_service = IndicatorLifecycleFacadeV500Alpha4()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/states")
async def states():
    return _service.states()

@router.post("/transition")
async def transition(indicator: str = "future_indicator_template", to_state: str = "validated"):
    return _service.transition(indicator, to_state)

@router.get("/rules")
async def rules():
    return _service.rules()

@router.get("/rollback-plan")
async def rollback_plan(indicator: str = "yasara"):
    return _service.rollback_plan(indicator)

@router.get("/audit-sample")
async def audit_sample():
    return _service.audit_sample()

@router.get("/contract")
async def contract():
    return _service.contract()
