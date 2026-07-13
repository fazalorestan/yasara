from fastapi import APIRouter
from app.v415_engine_registry_pro.registry import EngineRegistryProV415
from app.v415_neowave.models import NeoWaveRequestV415
from app.v415_neowave.service import NeoWaveEngineServiceV415

router = APIRouter(prefix="/v4-15/neowave", tags=["v4.15-neowave"])
_service = NeoWaveEngineServiceV415()
_registry = EngineRegistryProV415()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/engine-registry")
async def engine_registry():
    return _registry.list()

@router.get("/rules")
async def rules():
    return _service.rule_registry()

@router.post("/analyze")
async def analyze(request: NeoWaveRequestV415):
    return _service.analyze(request)

@router.get("/quick")
async def quick(symbol: str = "BTCUSDT", exchange: str = "binance", timeframe: str = "1m"):
    return _service.quick(symbol=symbol, exchange=exchange, timeframe=timeframe)
