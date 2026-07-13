from fastapi import APIRouter
from app.v41_indicator_engine.models import IndicatorRequestV41
from app.v41_indicator_engine.service import ModularIndicatorEngineServiceV41

router = APIRouter(prefix="/v4-1/indicator-engine", tags=["v4.1-indicator-engine"])
_service = ModularIndicatorEngineServiceV41()


@router.get("/summary")
async def summary():
    return _service.summary()


@router.get("/registry")
async def registry_status():
    return _service.registry_status()


@router.post("/analyze")
async def analyze(request: IndicatorRequestV41):
    return _service.analyze(request)


@router.get("/quick")
async def quick(symbol: str = "BTCUSDT", exchange: str = "binance", timeframe: str = "1m"):
    return _service.quick(symbol=symbol, exchange=exchange, timeframe=timeframe)
