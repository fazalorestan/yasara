from fastapi import APIRouter
from app.v40_market_context.models import AutoTradeGateRequestV40, MarketContextRequestV40
from app.v40_market_context.service import MarketContextServiceV40

router = APIRouter(prefix="/v4-0/market-context", tags=["v4.0-market-context"])
_service = MarketContextServiceV40()


@router.get("/summary")
async def summary():
    return _service.summary()


@router.get("/engines")
async def engines():
    return _service.engines()


@router.post("/context")
async def context(request: MarketContextRequestV40):
    return _service.context(request)


@router.get("/quick")
async def quick(symbol: str = "BTCUSDT", exchange: str = "binance"):
    return _service.context(MarketContextRequestV40(symbol=symbol, exchange=exchange))


@router.post("/autotrade-gate")
async def autotrade_gate(request: AutoTradeGateRequestV40):
    return _service.autotrade_gate(request)
