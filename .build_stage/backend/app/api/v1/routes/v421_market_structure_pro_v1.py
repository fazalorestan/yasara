from fastapi import APIRouter
from app.v421_market_structure_pro.models import MarketStructureProRequestV421
from app.v421_market_structure_pro.service import MarketStructureProServiceV421

router = APIRouter(prefix="/v4-21/market-structure-pro", tags=["v4.21-market-structure-pro"])
_service = MarketStructureProServiceV421()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.post("/analyze")
async def analyze(request: MarketStructureProRequestV421):
    return _service.analyze(request)

@router.get("/quick")
async def quick(symbol: str = "BTCUSDT", exchange: str = "binance", timeframe: str = "15m"):
    return _service.quick(symbol=symbol, exchange=exchange, timeframe=timeframe)
