from app.exchange_private_v1.domain.models import PrivateOrderRequest
from app.exchange_private_v1.infrastructure.binance_private_adapter import BinanceFuturesPrivateAdapterV1

class PrivateExchangeServiceV1:
    def __init__(self):
        self.binance = BinanceFuturesPrivateAdapterV1()

    async def place_order(self, request: PrivateOrderRequest):
        return await self.binance.place_order(request)

    async def balances(self, owner_id: str = "default"):
        return await self.binance.get_balances(owner_id)

    async def positions(self, owner_id: str = "default"):
        return await self.binance.get_positions(owner_id)

private_exchange_service_v1 = PrivateExchangeServiceV1()
