from fastapi import APIRouter
from app.v52_dashboard_provider_hub.service import dashboard_provider_hub

router = APIRouter(prefix="/enterprise/dashboard-hub", tags=["approved-dashboard"])

@router.get("/snapshot")
async def snapshot():
    return dashboard_provider_hub.snapshot()

@router.get("/providers")
async def providers():
    return dashboard_provider_hub.snapshot().providers

@router.get("/contract")
async def contract():
    return {
        "build_id":"2026.47.ENTERPRISE.001",
        "approved_dashboard_locked":True,
        "real_backend_data_only":True,
        "mock_data":False,
        "workspace_providers_hidden":True,
        "signal_only_default":True,
        "auto_trading_enabled":False,
    }
