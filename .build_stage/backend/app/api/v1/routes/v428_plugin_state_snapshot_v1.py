from fastapi import APIRouter
from app.v428_plugin_state_snapshot.service import PluginStateSnapshotServiceV428

router = APIRouter(prefix="/v4-28/plugin-state-snapshot", tags=["v4.28-plugin-state-snapshot"])
_service = PluginStateSnapshotServiceV428()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.post("/set-state")
async def set_state(plugin: str = "market_structure_pro", state: dict | None = None):
    return _service.set_state(plugin, state)

@router.get("/states")
async def states():
    return _service.states()

@router.get("/snapshot")
async def snapshot():
    return _service.snapshot()

@router.post("/restore-report")
async def restore_report(snapshot: dict):
    return _service.restore_report(snapshot)

@router.get("/extension-host-snapshot")
async def extension_host_snapshot():
    return _service.extension_host_snapshot()
