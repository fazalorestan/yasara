from fastapi import APIRouter
from app.v500_alpha31_1_patch_orchestrator.service import PatchOrchestratorFacadeV500Alpha311

router = APIRouter(prefix="/v5-0-alpha-31-1/patch-orchestrator", tags=["v5.0-alpha.31.1-patch-orchestrator"])
_service = PatchOrchestratorFacadeV500Alpha311()

@router.get("/summary")
async def summary(): return _service.summary()

@router.get("/contract")
async def contract(): return _service.contract()

@router.get("/safety")
async def safety(): return _service.safety()
