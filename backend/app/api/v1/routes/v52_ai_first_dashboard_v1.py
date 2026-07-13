from fastapi import APIRouter
from app.v52_ai_first_dashboard.service import ai_first_dashboard_service

router = APIRouter(prefix="/enterprise/ai-first-dashboard", tags=["ai-first-dashboard"])

@router.get("/snapshot")
async def snapshot():
    return ai_first_dashboard_service.snapshot()

@router.get("/doctor")
async def doctor():
    return ai_first_dashboard_service.snapshot().doctor

@router.get("/contract")
async def contract():
    return {
        "ready": True,
        "build_id": "2026.45.ENTERPRISE.001",
        "real_backend_data_only": True,
        "mock_data": False,
        "chart_priority": "secondary",
        "signal_priority": "primary",
        "signal_only_default": True,
        "auto_trading_enabled": False,
    }
