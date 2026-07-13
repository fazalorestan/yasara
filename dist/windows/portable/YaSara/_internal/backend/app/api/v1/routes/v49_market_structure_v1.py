from fastapi import APIRouter
from app.v49_market_structure.models import MarketStructureRequestV49
from app.v49_market_structure.service import ProfessionalMarketStructureServiceV49

router = APIRouter(prefix="/v4-9/market-structure", tags=["v4.9-market-structure"])
_service = ProfessionalMarketStructureServiceV49()


@router.get("/summary")
async def summary():
    return _service.summary()


@router.post("/analyze")
async def analyze(request: MarketStructureRequestV49):
    return _service.analyze(request)


@router.get("/quick")
async def quick(symbol: str = "BTCUSDT", exchange: str = "binance", timeframe: str = "1m"):
    return _service.quick(symbol=symbol, exchange=exchange, timeframe=timeframe)
