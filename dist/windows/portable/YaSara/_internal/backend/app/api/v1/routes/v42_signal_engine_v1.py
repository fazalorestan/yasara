from fastapi import APIRouter
from app.v42_signal_engine.models import SignalRequestV42
from app.v42_signal_engine.service import MultiLayerSignalEngineServiceV42

router = APIRouter(prefix="/v4-2/signal-engine", tags=["v4.2-signal-engine"])
_service = MultiLayerSignalEngineServiceV42()


@router.get("/summary")
async def summary():
    return _service.summary()


@router.post("/generate")
async def generate(request: SignalRequestV42):
    return _service.generate(request)


@router.get("/quick")
async def quick(symbol: str = "BTCUSDT", exchange: str = "binance", timeframe: str = "1m"):
    return _service.quick(symbol=symbol, exchange=exchange, timeframe=timeframe)
