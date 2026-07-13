from fastapi import APIRouter
from app.v500_alpha14_license_readiness.service import LicenseFinalReadinessFacadeV500Alpha14

router = APIRouter(prefix="/v5-0-alpha-14/license-readiness", tags=["v5.0-alpha.14-license-readiness"])
_service = LicenseFinalReadinessFacadeV500Alpha14()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/e2e")
async def e2e():
    return _service.e2e()

@router.get("/checklist")
async def checklist():
    return _service.checklist()

@router.get("/compatibility")
async def compatibility():
    return _service.compatibility()

@router.get("/handoff")
async def handoff():
    return _service.handoff()

@router.get("/gate")
async def gate():
    return _service.gate()

@router.get("/contract")
async def contract():
    return _service.contract()
