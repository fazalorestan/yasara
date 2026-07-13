from fastapi import APIRouter
from app.v34_market_analysis.models import MarketAnalysisRequestV34
from app.v34_market_analysis.service import MarketAnalysisEngineServiceV34

router = APIRouter(prefix="/v3-4/market-analysis", tags=["v3.4-market-analysis"])
_service = MarketAnalysisEngineServiceV34()


@router.get("/summary")
async def summary():
    return _service.summary()


@router.post("/analyze")
async def analyze(request: MarketAnalysisRequestV34):
    return _service.analyze(request)


@router.get("/quick")
async def quick(symbol: str = "BTCUSDT", exchange: str = "binance"):
    return _service.quick(symbol=symbol, exchange=exchange)
