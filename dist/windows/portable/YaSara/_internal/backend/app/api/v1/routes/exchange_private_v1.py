from fastapi import APIRouter
from app.exchange_private_v1.application.service import private_exchange_service_v1
from app.exchange_private_v1.domain.models import PrivateOrderRequest

router = APIRouter(prefix="/exchange-private-v1", tags=["exchange-private-v1"])

@router.post("/binance-futures/order")
async def place_binance_futures_order(payload: PrivateOrderRequest):
    return await private_exchange_service_v1.place_order(payload)

@router.get("/binance-futures/balances")
async def balances(owner_id: str = "default"):
    return await private_exchange_service_v1.balances(owner_id)

@router.get("/binance-futures/positions")
async def positions(owner_id: str = "default"):
    return await private_exchange_service_v1.positions(owner_id)
