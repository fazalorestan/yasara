from fastapi import APIRouter
from app.multi_exchange_v1.application.service import multi_exchange_service_v1
from app.multi_exchange_v1.domain.models import SupportedExchange
from app.multi_exchange_v1.health import ExchangeHealthEngineV1
from app.multi_exchange_v1.router_engine import ExchangeRouterEngineV1
from app.multi_exchange_v1.symbol_registry import symbol_registry_v1
from app.multi_exchange_v1.watchlist_feed import MultiExchangeWatchlistFeedV1, MultiExchangeWatchlistRequestV1

router = APIRouter(prefix="/multi-exchange-extras-v1", tags=["multi-exchange-extras-v1"])

@router.get("/symbols")
async def symbols(exchange: SupportedExchange | None = None):
    return symbol_registry_v1.list(exchange)

@router.get("/route")
async def route(symbol: str, preferred: SupportedExchange | None = None):
    return ExchangeRouterEngineV1().choose(symbol, preferred)

@router.get("/health")
async def health():
    return ExchangeHealthEngineV1().report()

@router.post("/watchlist")
async def watchlist(payload: MultiExchangeWatchlistRequestV1):
    return await MultiExchangeWatchlistFeedV1().build(payload, multi_exchange_service_v1)
