from fastapi import APIRouter
from app.v11_paper_trading.models import PaperOrderRequestV11
from app.v11_paper_trading.phase6_summary import V11Phase6SummaryBuilder
from app.v11_paper_trading.service import PaperTradingServiceV11

router = APIRouter(prefix="/v1-1/paper-trading", tags=["v1.1-paper-trading"])

_service = PaperTradingServiceV11()


@router.get("/summary")
async def summary():
    return V11Phase6SummaryBuilder().build()


@router.post("/orders")
async def submit_order(request: PaperOrderRequestV11, market_price: float | None = None):
    return _service.submit_order(request, market_price)


@router.get("/snapshot")
async def snapshot():
    return _service.snapshot()


@router.get("/demo")
async def demo():
    return PaperTradingServiceV11().demo()
