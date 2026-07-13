from fastapi import APIRouter
from app.v500_alpha32_1_definitive_patch_runner.service import DefinitivePatchRunnerFacadeV500Alpha321

router = APIRouter(prefix="/v5-0-alpha-32-1/definitive-patch-runner", tags=["v5.0-alpha.32.1-definitive-patch-runner"])
_service = DefinitivePatchRunnerFacadeV500Alpha321()

@router.get("/summary")
async def summary(): return _service.summary()

@router.get("/contract")
async def contract(): return _service.contract()

@router.get("/safety")
async def safety(): return _service.safety()
