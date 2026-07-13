from fastapi import APIRouter
from app.v439_enterprise_storage.service import EnterpriseStorageFacadeV439

router = APIRouter(prefix="/v4-39/enterprise-storage", tags=["v4.39-enterprise-storage"])
_service = EnterpriseStorageFacadeV439()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.post("/seed")
async def seed():
    return _service.seed()

@router.post("/artifact")
async def write_artifact(key: str = "artifact_latest", payload: dict | None = None):
    return _service.write_artifact(key, payload)

@router.post("/snapshot")
async def write_snapshot(key: str = "snapshot_latest", payload: dict | None = None):
    return _service.write_snapshot(key, payload)

@router.post("/backup")
async def write_backup(key: str = "backup_latest", payload: dict | None = None):
    return _service.write_backup(key, payload)

@router.get("/inventory")
async def inventory():
    return _service.inventory()

@router.get("/metrics")
async def metrics():
    return _service.metrics()

@router.get("/object-contract")
async def object_contract():
    return _service.object_contract()
