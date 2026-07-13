from fastapi import APIRouter
from app.v446_indicator_scanner_watchlist.service import IndicatorScannerWatchlistFacadeV446

router = APIRouter(prefix="/v4-46/indicator-scanner-watchlist", tags=["v4.46-indicator-scanner-watchlist"])
_service = IndicatorScannerWatchlistFacadeV446()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/sample")
async def sample():
    return _service.sample()

@router.get("/contract")
async def contract():
    return _service.contract()
