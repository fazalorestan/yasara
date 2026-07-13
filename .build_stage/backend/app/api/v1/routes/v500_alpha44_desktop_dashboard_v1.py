from fastapi import APIRouter
from app.v500_alpha44_desktop_dashboard.service import desktop_dashboard_facade_v500_alpha44 as _service

router = APIRouter(prefix="/v5-0-alpha-44/desktop-dashboard", tags=["v5.0-alpha.44-desktop-dashboard"])

@router.get("/summary")
async def summary(): return _service.summary()
@router.get("/contract")
async def contract(): return _service.contract()
@router.get("/view-model")
async def view_model(): return _service.view_model()
@router.get("/layout")
async def layout(): return _service.layout()
@router.get("/widgets")
async def widgets(): return _service.widgets()
@router.get("/refresh")
async def refresh(): return _service.refresh()
@router.get("/report")
async def report(): return _service.report()
@router.get("/readiness")
async def readiness(): return _service.readiness()
@router.get("/api-contract")
async def api_contract(): return _service.api_contract()
