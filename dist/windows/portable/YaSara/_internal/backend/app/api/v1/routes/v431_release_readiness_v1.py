from fastapi import APIRouter
from app.v431_release_readiness.service import ReleaseReadinessServiceV431

router = APIRouter(prefix="/v4-31/release-readiness", tags=["v4.31-release-readiness"])
_service = ReleaseReadinessServiceV431()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/gate")
async def gate():
    return _service.gate()

@router.get("/compatibility")
async def compatibility():
    return _service.compatibility()

@router.get("/plugins")
async def plugins():
    return _service.plugins()

@router.get("/security")
async def security():
    return _service.security()
