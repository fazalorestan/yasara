from fastapi import APIRouter, Query
from app.v52_ai_decision_engine.models import FusionRequest
from app.v52_ai_decision_engine.service import ai_decision_facade

router = APIRouter(prefix="/ai", tags=["ai-decision-core"])

@router.post("/fusion")
async def fusion(payload: FusionRequest):
    return ai_decision_facade.decide(payload)

@router.post("/decision")
async def decision(payload: FusionRequest):
    return ai_decision_facade.decide(payload)

@router.post("/confirmations")
async def confirmations(payload: FusionRequest):
    return ai_decision_facade.confirmations(payload)

@router.post("/explain")
async def explain(payload: FusionRequest):
    return ai_decision_facade.decide(payload).explanation

@router.get("/timeline")
async def timeline(limit: int = Query(default=100, ge=1, le=500)):
    return ai_decision_facade.timeline(limit)

@router.post("/keylevels")
async def keylevels(payload: dict):
    return ai_decision_facade.keylevels(payload)

@router.get("/strategy")
async def strategy():
    return {"strategies": ["scalp","day_trade","swing","trend","mean_reversion","momentum","breakout"]}

@router.get("/doctor")
async def doctor():
    return ai_decision_facade.doctor()

@router.get("/contract")
async def contract():
    return {
        "ready": True,
        "build_id": "2026.44.ENTERPRISE.001",
        "real_backend_data_only": True,
        "mock_data": False,
        "lazy_initialization": True,
        "service_registry": True,
        "auto_router_registry": True,
        "signal_only_default": True,
        "auto_trading_enabled": False,
    }
