from fastapi import APIRouter

from app.v52_alpha_legacy_marker_launcher_sync_diagnostics.service import (
    legacy_marker_launcher_sync_diagnostics_facade_v52_alpha as _service,
)

router = APIRouter(
    prefix="/v5-2-alpha/legacy-marker-launcher-sync-diagnostics",
    tags=["v5.2-alpha-legacy-marker-launcher-sync-diagnostics"],
)


@router.get("/summary")
async def summary():
    return _service.summary()


@router.get("/report")
async def report():
    return _service.report()


@router.get("/readiness")
async def readiness():
    return _service.readiness()


@router.get("/contract")
async def contract():
    return _service.contract()
