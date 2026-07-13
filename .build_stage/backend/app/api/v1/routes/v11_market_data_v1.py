from fastapi import APIRouter
from app.v11_market_data.models import SubscriptionRequestV11
from app.v11_market_data.phase1_summary import V11Phase1SummaryBuilder
from app.v11_market_data.service import MarketDataServiceV11
from app.v11_market_data.symbol_registry import SymbolRegistrySummaryBuilderV11

router = APIRouter(prefix="/v1-1/market-data", tags=["v1.1-market-data"])

_service = MarketDataServiceV11()
_service.bootstrap_demo()


@router.get("/summary")
async def summary():
    return V11Phase1SummaryBuilder().build()


@router.get("/snapshot")
async def snapshot():
    return _service.engine.snapshot()


@router.get("/status")
async def status():
    return _service.engine.status()


@router.get("/symbols")
async def symbols():
    return SymbolRegistrySummaryBuilderV11().build()


@router.post("/subscribe")
async def subscribe(request: SubscriptionRequestV11):
    return _service.engine.subscribe(request)


@router.post("/demo-ticker")
async def demo_ticker(exchange: str, symbol: str, last_price: float = 100.0):
    return _service.engine.ingest_synthetic_ticker(exchange, symbol, last_price)
