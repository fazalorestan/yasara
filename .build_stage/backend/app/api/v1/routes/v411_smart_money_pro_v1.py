from fastapi import APIRouter
from app.v411_smart_money_pro.models import SmartMoneyProRequestV411
from app.v411_smart_money_pro.service import SmartMoneyProServiceV411

router = APIRouter(prefix="/v4-11/smart-money-pro", tags=["v4.11-smart-money-pro"])
_service = SmartMoneyProServiceV411()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.post("/analyze")
async def analyze(request: SmartMoneyProRequestV411):
    return _service.analyze(request)

@router.get("/quick")
async def quick(symbol: str = "BTCUSDT", exchange: str = "binance", timeframe: str = "1m"):
    return _service.quick(symbol=symbol, exchange=exchange, timeframe=timeframe)
