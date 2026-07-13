from fastapi import APIRouter
from app.v11_operations.phase5_summary import V11Phase5SummaryBuilder
from app.v11_operations.service import OperationsMaintenanceServiceV11

router = APIRouter(prefix="/v1-1/operations", tags=["v1.1-operations"])

_service = OperationsMaintenanceServiceV11()


@router.get("/summary")
async def summary():
    return V11Phase5SummaryBuilder().build()


@router.get("/cleanup-policy")
async def cleanup_policy(deep: bool = False):
    return _service.cleanup_policy(deep)


@router.get("/health")
async def health():
    return _service.health()


@router.get("/project-info")
async def project_info():
    return _service.info()


@router.get("/release-verification")
async def release_verification():
    return _service.release()
