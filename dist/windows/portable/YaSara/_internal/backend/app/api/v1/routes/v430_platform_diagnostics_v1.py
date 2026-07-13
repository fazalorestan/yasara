from fastapi import APIRouter
from app.v430_platform_diagnostics.service import PlatformDiagnosticsServiceV430

router = APIRouter(prefix="/v4-30/platform-diagnostics", tags=["v4.30-platform-diagnostics"])
_service = PlatformDiagnosticsServiceV430()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/readiness")
async def readiness():
    return _service.readiness()

@router.get("/paths")
async def paths():
    return _service.paths()

@router.get("/manifests")
async def manifests():
    return _service.manifests()

@router.get("/registry")
async def registry():
    return _service.registry()

@router.get("/runtime")
async def runtime():
    return _service.runtime()

@router.get("/api-health")
async def api_health():
    return _service.api_health()
