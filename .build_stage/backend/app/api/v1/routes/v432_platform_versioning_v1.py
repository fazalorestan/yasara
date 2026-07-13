from fastapi import APIRouter
from app.v432_platform_versioning.service import PlatformVersioningServiceV432

router = APIRouter(prefix="/v4-32/platform-versioning", tags=["v4.32-platform-versioning"])
_service = PlatformVersioningServiceV432()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/versions")
async def versions():
    return _service.versions()

@router.get("/migrations")
async def migrations():
    return _service.migrations()

@router.get("/compatibility")
async def compatibility():
    return _service.compatibility()

@router.get("/deprecation")
async def deprecation():
    return _service.deprecation()

@router.get("/upgrade-path")
async def upgrade_path():
    return _service.upgrade_path()
