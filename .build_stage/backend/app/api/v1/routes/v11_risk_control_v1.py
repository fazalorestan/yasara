from fastapi import APIRouter
from app.v11_paper_trading.models import PaperOrderRequestV11
from app.v11_risk_control.phase7_summary import V11Phase7SummaryBuilder
from app.v11_risk_control.service import RiskControlServiceV11

router = APIRouter(prefix="/v1-1/risk-control", tags=["v1.1-risk-control"])

_service = RiskControlServiceV11()


@router.get("/summary")
async def summary():
    return V11Phase7SummaryBuilder().build()


@router.get("/rules")
async def rules():
    return _service.rules()


@router.get("/status")
async def status():
    return _service.status()


@router.post("/paper-order")
async def paper_order(request: PaperOrderRequestV11, market_price: float | None = None):
    return _service.submit_guarded_order(request, market_price)
