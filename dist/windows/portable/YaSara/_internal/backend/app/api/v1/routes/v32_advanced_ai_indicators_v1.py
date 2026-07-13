from fastapi import APIRouter
from app.v32_advanced_ai_indicators.models import AdvancedIndicatorRequestV32
from app.v32_advanced_ai_indicators.service import AdvancedAIIndicatorServiceV32

router = APIRouter(prefix="/v3-2/ai-indicators", tags=["v3.2-ai-indicators"])
_service = AdvancedAIIndicatorServiceV32()


@router.get("/summary")
async def summary():
    return _service.summary()


@router.post("/analyze")
async def analyze(request: AdvancedIndicatorRequestV32):
    return _service.analyze(request)


@router.get("/quick")
async def quick(symbol: str = "BTCUSDT", exchange: str = "binance", timeframe: str = "1m", limit: int = 120):
    return _service.analyze(AdvancedIndicatorRequestV32(symbol=symbol, exchange=exchange, timeframe=timeframe, limit=limit))


@router.get("/batch")
async def batch():
    return _service.batch()
