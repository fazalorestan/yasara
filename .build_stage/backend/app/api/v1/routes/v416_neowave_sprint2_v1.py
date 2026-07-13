from fastapi import APIRouter
from app.v416_neowave_sprint2.models import NeoWaveSprint2RequestV416
from app.v416_neowave_sprint2.service import NeoWaveSprint2ServiceV416

router = APIRouter(prefix="/v4-16/neowave-sprint2", tags=["v4.16-neowave-sprint2"])
_service = NeoWaveSprint2ServiceV416()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.post("/analyze")
async def analyze(request: NeoWaveSprint2RequestV416):
    return _service.analyze(request)

@router.get("/quick")
async def quick(symbol: str = "BTCUSDT", exchange: str = "binance", timeframe: str = "1m"):
    return _service.quick(symbol=symbol, exchange=exchange, timeframe=timeframe)
