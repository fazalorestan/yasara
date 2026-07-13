from fastapi import APIRouter
from app.v11_ai_market_intelligence.phase3_summary import V11Phase3SummaryBuilder
from app.v11_ai_market_intelligence.service import AIMarketIntelligenceServiceV11

router = APIRouter(prefix="/v1-1/ai-market-intelligence", tags=["v1.1-ai-market-intelligence"])

_service = AIMarketIntelligenceServiceV11()


@router.get("/summary")
async def summary():
    return V11Phase3SummaryBuilder().build()


@router.get("/dashboard")
async def dashboard():
    return _service.dashboard_payload()


@router.get("/insights")
async def insights():
    return _service.demo_insights()
