from fastapi import APIRouter
from app.v35_smart_money.models import SmartMoneyRequestV35
from app.v35_smart_money.service import SmartMoneyEngineServiceV35

router = APIRouter(prefix="/v3-5/smart-money", tags=["v3.5-smart-money"])
_service = SmartMoneyEngineServiceV35()


@router.get("/summary")
async def summary():
    return _service.summary()


@router.post("/analyze")
async def analyze(request: SmartMoneyRequestV35):
    return _service.analyze(request)


@router.get("/quick")
async def quick(symbol: str = "BTCUSDT", exchange: str = "binance", timeframe: str = "1m"):
    return _service.quick(symbol=symbol, exchange=exchange, timeframe=timeframe)
