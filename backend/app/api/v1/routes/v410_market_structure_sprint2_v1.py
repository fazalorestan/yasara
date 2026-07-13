from fastapi import APIRouter
from app.v410_market_structure_sprint2.models import MarketStructureSprint2RequestV410
from app.v410_market_structure_sprint2.service import MarketStructureSprint2ServiceV410

router = APIRouter(prefix="/v4-10/market-structure-sprint2", tags=["v4.10-market-structure-sprint2"])
_service = MarketStructureSprint2ServiceV410()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.post("/analyze")
async def analyze(request: MarketStructureSprint2RequestV410):
    return _service.analyze(request)

@router.get("/quick")
async def quick(symbol: str = "BTCUSDT", exchange: str = "binance"):
    return _service.quick(symbol=symbol, exchange=exchange)
