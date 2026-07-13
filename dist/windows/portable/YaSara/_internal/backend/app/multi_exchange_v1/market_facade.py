from app.multi_exchange_v1.cache import MarketDataCacheV1
from app.multi_exchange_v1.domain.models import SupportedExchange
from app.multi_exchange_v1.application.service import MultiExchangeServiceV1

class CachedMarketDataFacadeV1:
    def __init__(self, service: MultiExchangeServiceV1 | None = None, cache: MarketDataCacheV1 | None = None):
        self.service = service or MultiExchangeServiceV1()
        self.cache = cache or MarketDataCacheV1(ttl_seconds=10)

    async def ticker(self, exchange: SupportedExchange, symbol: str):
        key = f"ticker:{exchange}:{symbol.upper()}"
        cached = self.cache.get(key)
        if cached is not None:
            return cached
        result = await self.service.ticker(exchange, symbol)
        return self.cache.set(key, result)

    async def order_book(self, exchange: SupportedExchange, symbol: str, limit: int = 20):
        key = f"book:{exchange}:{symbol.upper()}:{limit}"
        cached = self.cache.get(key)
        if cached is not None:
            return cached
        result = await self.service.order_book(exchange, symbol, limit)
        return self.cache.set(key, result)
