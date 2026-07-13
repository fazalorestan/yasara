from fastapi import APIRouter
from app.v23_exchange_connector.service import ExchangeConnectorServiceV23

router = APIRouter(prefix="/v2-3/exchange-connector", tags=["v2.3-exchange-connector"])
_service = ExchangeConnectorServiceV23()


@router.get("/summary")
async def summary():
    return _service.summary()


@router.get("/capabilities")
async def capabilities():
    return _service.capabilities()


@router.get("/quote")
async def quote(symbol: str = "BTCUSDT", exchange: str = "binance"):
    return _service.quote(symbol=symbol, exchange=exchange)


@router.get("/ohlc")
async def ohlc(symbol: str = "BTCUSDT", exchange: str = "binance", timeframe: str = "4H", limit: int = 120):
    return _service.ohlc_live_ready(symbol=symbol, exchange=exchange, timeframe=timeframe, limit=limit)


@router.get("/orderbook")
async def orderbook(symbol: str = "BTCUSDT", exchange: str = "binance"):
    return _service.orderbook(symbol=symbol, exchange=exchange)
