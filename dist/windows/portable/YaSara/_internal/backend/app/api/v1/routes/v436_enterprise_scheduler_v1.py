from fastapi import APIRouter
from app.v436_enterprise_scheduler.service import EnterpriseSchedulerServiceV436

router = APIRouter(prefix="/v4-36/enterprise-scheduler", tags=["v4.36-enterprise-scheduler"])
_service = EnterpriseSchedulerServiceV436()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/tasks")
async def tasks():
    return _service.tasks()

@router.post("/seed")
async def seed():
    return _service.seed()

@router.post("/run-once")
async def run_once(task: str = "diagnostics_snapshot"):
    return _service.run_once(task)

@router.get("/status")
async def status():
    return _service.status()

@router.get("/retry-policies")
async def retry_policies():
    return _service.retry_policies()

@router.get("/metrics")
async def metrics():
    return _service.metrics()
