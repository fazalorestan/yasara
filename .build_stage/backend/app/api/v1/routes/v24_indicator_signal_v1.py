from fastapi import APIRouter
from app.v24_indicator_signal.service import IndicatorSignalServiceV24

router = APIRouter(prefix="/v2-4/indicator-signal", tags=["v2.4-indicator-signal"])
_service = IndicatorSignalServiceV24()


@router.get("/summary")
async def summary():
    return _service.summary()


@router.get("/snapshot")
async def snapshot(symbol: str = "BTCUSDT", exchange: str = "binance", timeframe: str = "4H"):
    return _service.snapshot(symbol=symbol, exchange=exchange, timeframe=timeframe)


@router.get("/batch")
async def batch(exchange: str = "all"):
    return _service.batch(exchange=exchange)
