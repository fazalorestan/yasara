from fastapi import APIRouter
from app.v500_alpha36_plugin_enterprise.service import PluginEnterpriseFacadeV500Alpha36

router = APIRouter(prefix="/v5-0-alpha-36/plugin-enterprise", tags=["v5.0-alpha.36-plugin-enterprise"])
_service = PluginEnterpriseFacadeV500Alpha36()

@router.get("/summary")
async def summary(): return _service.summary()
@router.get("/security")
async def security(): return _service.security()
@router.get("/performance")
async def performance(): return _service.performance()
@router.get("/quality-score")
async def quality_score(): return _service.quality_score()
@router.get("/runtime-acceptance")
async def runtime_acceptance(): return _service.runtime_acceptance()
@router.get("/final-report")
async def final_report(): return _service.final_report()
@router.get("/final-status")
async def final_status(): return _service.final_status()
@router.get("/readiness")
async def readiness(): return _service.readiness()
@router.get("/contract")
async def contract(): return _service.contract()
