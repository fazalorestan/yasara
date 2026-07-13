from fastapi import APIRouter
from app.v437_enterprise_queue.service import EnterpriseQueueFacadeV437

router = APIRouter(prefix="/v4-37/enterprise-queue", tags=["v4.37-enterprise-queue"])
_service = EnterpriseQueueFacadeV437()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.post("/seed")
async def seed():
    return _service.seed()

@router.post("/enqueue")
async def enqueue(topic: str = "diagnostics", payload: dict | None = None, priority: int = 5):
    return _service.enqueue(topic, payload, priority)

@router.post("/dequeue")
async def dequeue():
    return _service.dequeue()

@router.get("/snapshot")
async def snapshot():
    return _service.snapshot()

@router.get("/metrics")
async def metrics():
    return _service.metrics()
