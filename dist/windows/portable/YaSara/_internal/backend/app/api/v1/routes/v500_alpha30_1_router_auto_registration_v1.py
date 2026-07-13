from fastapi import APIRouter
from app.v500_alpha30_1_router_auto_registration.service import RouterAutoRegistrationFacadeV500Alpha301

router = APIRouter(prefix="/v5-0-alpha-30-1/router-auto-registration", tags=["v5.0-alpha.30.1-router-auto-registration"])
_service = RouterAutoRegistrationFacadeV500Alpha301()

@router.get("/summary")
async def summary(): return _service.summary()
@router.get("/discover")
async def discover(): return _service.discover()
@router.get("/inspect-sample")
async def inspect_sample(): return _service.inspect_sample()
@router.get("/plan")
async def plan(): return _service.plan()
@router.get("/helper")
async def helper(): return _service.helper()
@router.get("/manifest")
async def manifest(): return _service.manifest()
@router.get("/audit-sample")
async def audit_sample(): return _service.audit_sample()
@router.get("/readiness")
async def readiness(): return _service.readiness()
@router.get("/contract")
async def contract(): return _service.contract()
