from fastapi import APIRouter
from app.v412_smart_money_pro_sprint2.models import SmartMoneyProSprint2RequestV412
from app.v412_smart_money_pro_sprint2.service import SmartMoneyProSprint2ServiceV412

router = APIRouter(prefix="/v4-12/smart-money-pro-sprint2", tags=["v4.12-smart-money-pro-sprint2"])
_service = SmartMoneyProSprint2ServiceV412()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.post("/analyze")
async def analyze(request: SmartMoneyProSprint2RequestV412):
    return _service.analyze(request)

@router.get("/quick")
async def quick(symbol: str = "BTCUSDT", exchange: str = "binance", timeframe: str = "1m"):
    return _service.quick(symbol=symbol, exchange=exchange, timeframe=timeframe)
