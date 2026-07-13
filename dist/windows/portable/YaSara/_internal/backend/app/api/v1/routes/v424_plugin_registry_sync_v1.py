from fastapi import APIRouter
from app.v424_plugin_registry_sync.service import PluginRegistrySyncFacadeV424

router = APIRouter(prefix="/v4-24/plugin-registry-sync", tags=["v4.24-plugin-registry-sync"])
_service = PluginRegistrySyncFacadeV424()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.post("/sync")
async def sync():
    return _service.sync()

@router.get("/lifecycle")
async def lifecycle():
    return _service.lifecycle()

@router.get("/governance")
async def governance():
    return _service.governance()
