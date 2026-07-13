from fastapi import APIRouter
from app.v433_operations_runbook.service import OperationsRunbookServiceV433

router = APIRouter(prefix="/v4-33/operations-runbook", tags=["v4.33-operations-runbook"])
_service = OperationsRunbookServiceV433()

@router.get("/summary")
async def summary(): return _service.summary()

@router.get("/runbook")
async def runbook(): return _service.runbook()

@router.get("/incident-response")
async def incident_response(): return _service.incident_response()

@router.get("/rollback")
async def rollback(): return _service.rollback()

@router.get("/recovery")
async def recovery(): return _service.recovery()

@router.get("/status")
async def status(): return _service.status()
