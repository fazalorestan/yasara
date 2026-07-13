from fastapi import APIRouter
from app.v11_alerts.phase8_summary import V11Phase8SummaryBuilder
from app.v11_alerts.service import AlertsNotificationServiceV11

router = APIRouter(prefix="/v1-1/alerts", tags=["v1.1-alerts"])

_service = AlertsNotificationServiceV11()


@router.get("/summary")
async def summary():
    return V11Phase8SummaryBuilder().build()


@router.post("/rules/price")
async def create_price_rule(symbol: str, above: float | None = None, below: float | None = None):
    return _service.create_price_rule(symbol, above, below)


@router.post("/evaluate-price")
async def evaluate_price(symbol: str, price: float):
    return _service.evaluate_price(symbol, price)


@router.post("/risk-block")
async def risk_block(message: str, symbol: str | None = None):
    return _service.emit_risk_block(message, symbol)


@router.get("/snapshot")
async def snapshot():
    return _service.snapshot()


@router.get("/demo")
async def demo():
    return AlertsNotificationServiceV11().demo()
