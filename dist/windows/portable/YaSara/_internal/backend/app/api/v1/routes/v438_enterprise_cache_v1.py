from fastapi import APIRouter
from app.v438_enterprise_cache.service import EnterpriseCacheFacadeV438

router = APIRouter(prefix="/v4-38/enterprise-cache", tags=["v4.38-enterprise-cache"])
_service = EnterpriseCacheFacadeV438()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.post("/seed")
async def seed():
    return _service.seed()

@router.post("/set")
async def set_cache(key: str = "diagnostics", value: str = "ready", ttl_seconds: int = 300):
    return _service.set(key, value, ttl_seconds)

@router.get("/get")
async def get_cache(key: str = "diagnostics"):
    return _service.get(key)

@router.get("/snapshot")
async def snapshot():
    return _service.snapshot()

@router.get("/metrics")
async def metrics():
    return _service.metrics()

@router.post("/invalidate")
async def invalidate(key: str = "diagnostics"):
    return _service.invalidate(key)

@router.get("/redis-contract")
async def redis_contract():
    return _service.redis_contract()
