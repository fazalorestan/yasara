from fastapi import APIRouter
from app.v500_alpha15_market_data.service import MarketDataFacadeV500Alpha15

router = APIRouter(prefix="/v5-0-alpha-15/market-data", tags=["v5.0-alpha.15-market-data"])
_service = MarketDataFacadeV500Alpha15()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/symbols")
async def symbols():
    return _service.symbols()

@router.get("/symbol")
async def symbol(symbol: str = "BTCUSDT"):
    return _service.symbol(symbol)

@router.get("/samples")
async def samples(symbol: str = "BTCUSDT"):
    return _service.samples(symbol)

@router.get("/validate-sample")
async def validate_sample(symbol: str = "BTCUSDT"):
    return _service.validate_sample(symbol)

@router.get("/readiness")
async def readiness():
    return _service.readiness()

@router.get("/contract")
async def contract():
    return _service.contract()
