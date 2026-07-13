from fastapi import APIRouter
from app.final_operations_v1.operational_status import OperationalStatusBuilderV1
from app.final_operations_v1.runbook import OperationalRunbookBuilderV1
from app.final_operations_v1.troubleshooting import TroubleshootingGuideBuilderV1
from app.final_operations_v1.support_matrix import SupportMatrixBuilderV1

router = APIRouter(prefix="/final-operations-v1", tags=["final-operations-v1"])

@router.get("/status")
async def status():
    return OperationalStatusBuilderV1().build()

@router.get("/runbook")
async def runbook():
    return OperationalRunbookBuilderV1().build()

@router.get("/troubleshooting")
async def troubleshooting():
    return TroubleshootingGuideBuilderV1().build()

@router.get("/support-matrix")
async def support_matrix():
    return SupportMatrixBuilderV1().build()
