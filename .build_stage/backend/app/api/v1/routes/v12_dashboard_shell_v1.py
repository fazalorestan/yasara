from fastapi import APIRouter
from app.v12_dashboard.service import DashboardShellServiceV12

router = APIRouter(prefix="/v1-2/dashboard-shell", tags=["v1.2-dashboard-shell"])

_service = DashboardShellServiceV12()


@router.get("/summary")
async def summary():
    return _service.summary()
