from fastapi import APIRouter
from app.v413_ict_engine.models import ICTEngineRequestV413
from app.v413_ict_engine.service import ICTEngineServiceV413

router = APIRouter(prefix="/v4-13/ict-engine", tags=["v4.13-ict-engine"])
_service = ICTEngineServiceV413()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.post("/analyze")
async def analyze(request: ICTEngineRequestV413):
    return _service.analyze(request)

@router.get("/quick")
async def quick(symbol: str = "BTCUSDT", exchange: str = "binance", timeframe: str = "1m"):
    return _service.quick(symbol=symbol, exchange=exchange, timeframe=timeframe)
