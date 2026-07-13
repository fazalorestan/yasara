from fastapi import APIRouter
from app.v11_exchange_connectivity.phase2_summary import V11Phase2SummaryBuilder
from app.v11_exchange_connectivity.service import ExchangeConnectivityServiceV11

router = APIRouter(prefix="/v1-1/exchange-connectivity", tags=["v1.1-exchange-connectivity"])

_service = ExchangeConnectivityServiceV11()


@router.get("/summary")
async def summary():
    return V11Phase2SummaryBuilder().build()


@router.get("/diagnostics")
async def diagnostics():
    return _service.diagnostics()


@router.get("/health")
async def health():
    return _service.health.check_all()


@router.get("/market-request")
async def market_request(path: str = "/api/v3/ticker/price", preferred_exchange: str | None = "binance"):
    return _service.router.market_request(path, preferred_exchange)
