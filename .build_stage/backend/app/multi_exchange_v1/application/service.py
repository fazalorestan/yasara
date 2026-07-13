from app.multi_exchange_v1.domain.models import SupportedExchange, UnifiedPrivateOrderRequest
from app.multi_exchange_v1.registry import exchange_registry_v1

class MultiExchangeServiceV1:
    async def list_exchanges(self):
        return exchange_registry_v1.descriptors()

    async def ticker(self, exchange: SupportedExchange, symbol: str):
        adapter = exchange_registry_v1.get(exchange)
        if adapter is None:
            return None
        return await adapter.ticker(symbol)

    async def order_book(self, exchange: SupportedExchange, symbol: str, limit: int = 20):
        adapter = exchange_registry_v1.get(exchange)
        if adapter is None:
            return None
        return await adapter.order_book(symbol, limit)

    async def dry_run_order(self, request: UnifiedPrivateOrderRequest):
        adapter = exchange_registry_v1.get(request.exchange)
        if adapter is None:
            return None
        return await adapter.place_order_dry_run(request)

multi_exchange_service_v1 = MultiExchangeServiceV1()
