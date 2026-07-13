from fastapi import APIRouter
from app.v417_elliott.models import ElliottRequestV417
from app.v417_elliott.service import ElliottEngineServiceV417

router = APIRouter(prefix="/v4-17/elliott", tags=["v4.17-elliott"])
_service = ElliottEngineServiceV417()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/rules")
async def rules():
    return _service.rule_registry()

@router.post("/analyze")
async def analyze(request: ElliottRequestV417):
    return _service.analyze(request)

@router.get("/quick")
async def quick(symbol: str = "BTCUSDT", exchange: str = "binance", timeframe: str = "1m"):
    return _service.quick(symbol=symbol, exchange=exchange, timeframe=timeframe)
