from fastapi import APIRouter

from app.v52_enterprise_trading_os.service import enterprise_trading_os_service

router = APIRouter(
    prefix="/enterprise/trading-os",
    tags=["enterprise-trading-os"],
)


@router.get("/snapshot")
async def snapshot():
    return enterprise_trading_os_service.snapshot()


@router.get("/doctor")
async def doctor():
    return enterprise_trading_os_service.snapshot().doctor


@router.get("/contract")
async def contract():
    return {
        "ready": True,
        "build_id": "2026.43.ENTERPRISE.001",
        "real_data_only": True,
        "mock_data": False,
        "workspaces": ["trader", "ai", "portfolio", "developer"],
        "signal_only_default": True,
        "auto_trading_enabled": False,
    }
