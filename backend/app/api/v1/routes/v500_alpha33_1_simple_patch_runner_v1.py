from fastapi import APIRouter
from app.v500_alpha33_1_simple_patch_runner.service import SimplePatchRunnerFacadeV500Alpha331
router = APIRouter(prefix="/v5-0-alpha-33-1/simple-patch-runner", tags=["v5.0-alpha.33.1-simple-patch-runner"])
_service = SimplePatchRunnerFacadeV500Alpha331()
@router.get("/summary")
async def summary(): return _service.summary()
@router.get("/contract")
async def contract(): return _service.contract()
@router.get("/safety")
async def safety(): return _service.safety()
