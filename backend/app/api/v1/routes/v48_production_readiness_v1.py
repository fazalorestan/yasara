from fastapi import APIRouter
from app.v48_production_readiness.models import BuildProfileRequestV48
from app.v48_production_readiness.service import ProductionReadinessServiceV48

router = APIRouter(prefix="/v4-8/production-readiness", tags=["v4.8-production-readiness"])
_service = ProductionReadinessServiceV48()


@router.get("/summary")
async def summary():
    return _service.summary()


@router.get("/manifest")
async def manifest():
    return _service.manifest()


@router.post("/build-profile-guard")
async def build_profile_guard(request: BuildProfileRequestV48):
    return _service.build_profile_guard(request)


@router.get("/environment-health")
async def environment_health():
    return _service.environment_health()


@router.get("/security-checklist")
async def security_checklist():
    return _service.security_checklist()


@router.get("/backup-status")
async def backup_status():
    return _service.backup_status()


@router.get("/final-readiness")
async def final_readiness():
    return _service.final_readiness()
