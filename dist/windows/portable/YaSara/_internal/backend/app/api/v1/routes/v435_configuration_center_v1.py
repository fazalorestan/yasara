from fastapi import APIRouter
from app.v435_configuration_center.service import ConfigurationCenterServiceV435

router = APIRouter(prefix="/v4-35/configuration-center", tags=["v4.35-configuration-center"])
_service = ConfigurationCenterServiceV435()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/profiles")
async def profiles():
    return _service.profiles()

@router.get("/runtime")
async def runtime():
    return _service.runtime()

@router.post("/runtime")
async def set_runtime(key: str, value: str):
    return _service.set_runtime(key, value)

@router.get("/validate")
async def validate():
    return _service.validate()

@router.get("/secrets")
async def secrets():
    return _service.secrets()

@router.post("/commit")
async def commit(label: str = "manual"):
    return _service.commit(label)

@router.get("/snapshot")
async def snapshot():
    return _service.snapshot()
