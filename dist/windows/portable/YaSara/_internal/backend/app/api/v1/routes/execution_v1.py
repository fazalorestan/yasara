from fastapi import APIRouter
from app.execution_v1.application.service import execution_service_v1
from app.execution_v1.domain.models import ExecutionIntent

router = APIRouter(prefix="/execution-v1", tags=["execution-v1"])

@router.post("/execute")
async def execute_intent(intent: ExecutionIntent):
    return await execution_service_v1.execute(intent)

@router.get("/audit")
async def audit_log():
    return await execution_service_v1.audit_log()
