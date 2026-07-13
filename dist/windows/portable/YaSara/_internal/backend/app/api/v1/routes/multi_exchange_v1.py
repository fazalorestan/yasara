from fastapi import APIRouter, HTTPException
from app.multi_exchange_v1.application.service import multi_exchange_service_v1
from app.multi_exchange_v1.domain.models import SupportedExchange, UnifiedPrivateOrderRequest

router = APIRouter(prefix="/multi-exchange-v1", tags=["multi-exchange-v1"])

@router.get("/exchanges")
async def list_exchanges():
    return await multi_exchange_service_v1.list_exchanges()

@router.get("/{exchange}/ticker")
async def ticker(exchange: SupportedExchange, symbol: str):
    result = await multi_exchange_service_v1.ticker(exchange, symbol)
    if result is None:
        raise HTTPException(status_code=404, detail="Exchange adapter not found")
    return result

@router.get("/{exchange}/order-book")
async def order_book(exchange: SupportedExchange, symbol: str, limit: int = 20):
    result = await multi_exchange_service_v1.order_book(exchange, symbol, limit)
    if result is None:
        raise HTTPException(status_code=404, detail="Exchange adapter not found")
    return result

@router.post("/dry-run-order")
async def dry_run_order(payload: UnifiedPrivateOrderRequest):
    result = await multi_exchange_service_v1.dry_run_order(payload)
    if result is None:
        raise HTTPException(status_code=404, detail="Exchange adapter not found")
    return result
