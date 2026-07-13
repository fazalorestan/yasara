from fastapi import APIRouter
from app.v31_live_exchange.models import LiveSubscriptionV31
from app.v31_live_exchange.service import LiveExchangeServiceV31

router = APIRouter(prefix="/v3-1/live-exchange", tags=["v3.1-live-exchange"])
_service = LiveExchangeServiceV31()


@router.get("/summary")
async def summary():
    return _service.summary()


@router.get("/exchanges")
async def supported_exchanges():
    return _service.supported_exchanges()


@router.post("/subscribe")
async def subscribe(sub: LiveSubscriptionV31):
    return _service.subscribe(sub)


@router.delete("/unsubscribe")
async def unsubscribe(exchange: str = "binance", symbol: str = "BTCUSDT", timeframe: str = "1m"):
    return _service.unsubscribe(exchange=exchange, symbol=symbol, timeframe=timeframe)


@router.get("/tick")
async def live_tick(symbol: str = "BTCUSDT", exchange: str = "binance"):
    return _service.live_tick(symbol=symbol, exchange=exchange)


@router.get("/orderbook")
async def live_orderbook(symbol: str = "BTCUSDT", exchange: str = "binance"):
    return _service.live_orderbook(symbol=symbol, exchange=exchange)


@router.get("/candles")
async def live_candles(symbol: str = "BTCUSDT", exchange: str = "binance", timeframe: str = "1m", limit: int = 100):
    return _service.live_candles(symbol=symbol, exchange=exchange, timeframe=timeframe, limit=limit)


@router.get("/status")
async def realtime_status():
    return _service.realtime_status()
