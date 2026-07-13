from fastapi import APIRouter
from app.v500_alpha3_indicator_sandbox.service import IndicatorSandboxFacadeV500Alpha3

router = APIRouter(prefix="/v5-0-alpha-3/indicator-sandbox", tags=["v5.0-alpha.3-indicator-sandbox"])
_service = IndicatorSandboxFacadeV500Alpha3()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/policy")
async def policy():
    return _service.policy()

@router.get("/validate-manifest")
async def validate_manifest():
    return _service.validate_manifest()

@router.get("/validate-runtime")
async def validate_runtime():
    return _service.validate_runtime()

@router.get("/install-gate")
async def install_gate():
    return _service.install_gate()

@router.get("/contract")
async def contract():
    return _service.contract()
