from fastapi import APIRouter

from app.v52_alpha_baseline_syntax_recovery.service import (
    baseline_syntax_recovery_facade_v52_alpha as _service,
)

router = APIRouter(
    prefix="/v5-2-alpha/baseline-syntax-recovery",
    tags=["v5.2-alpha-baseline-syntax-recovery"],
)


@router.get("/summary")
async def summary():
    return _service.summary()


@router.get("/report")
async def report():
    return _service.report()


@router.get("/readiness")
async def readiness():
    return _service.readiness()


@router.get("/contract")
async def contract():
    return _service.contract()
