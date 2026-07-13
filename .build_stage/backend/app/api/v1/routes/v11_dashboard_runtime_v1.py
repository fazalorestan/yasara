from fastapi import APIRouter
from app.v11_dashboard_runtime.phase4_summary import V11Phase4SummaryBuilder
from app.v11_dashboard_runtime.snapshot_service import DashboardRuntimeServiceV11

router = APIRouter(prefix="/v1-1/dashboard-runtime", tags=["v1.1-dashboard-runtime"])

_service = DashboardRuntimeServiceV11()


@router.get("/summary")
async def summary():
    return V11Phase4SummaryBuilder().build()


@router.get("/snapshot")
async def snapshot():
    return _service.snapshot()


@router.get("/panels")
async def panels():
    return _service.snapshot().panels


@router.get("/alerts")
async def alerts():
    return _service.snapshot().alerts
