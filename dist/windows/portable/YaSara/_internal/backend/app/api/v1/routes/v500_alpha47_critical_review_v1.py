from fastapi import APIRouter
from app.v500_alpha47_critical_review.service import critical_review_facade as _service

router = APIRouter(
    prefix="/v5-0-alpha-47/critical-review",
    tags=["v5.0-alpha.47-critical-review"],
)

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/trading-mode")
async def trading_mode(auto_trading_enabled: bool = False, signal_only_mode: bool = True):
    return _service.trading_mode(
        auto_trading_enabled=auto_trading_enabled,
        signal_only_mode=signal_only_mode,
    )

@router.get("/correlation-health")
async def correlation_health(valid: bool = True):
    return _service.correlation_health({"valid": valid})

@router.get("/fail-closed-demo")
async def fail_closed_demo(
    risk_engine: bool = True,
    correlation_engine: bool = True,
    position_manager: bool = True,
    exchange: bool = True,
    database: bool = True,
):
    return _service.fail_closed({
        "risk_engine": risk_engine,
        "correlation_engine": correlation_engine,
        "position_manager": position_manager,
        "exchange": exchange,
        "database": database,
    })
