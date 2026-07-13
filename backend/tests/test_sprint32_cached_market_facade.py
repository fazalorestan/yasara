import pytest
from app.multi_exchange_v1.domain.models import SupportedExchange
from app.multi_exchange_v1.market_facade import CachedMarketDataFacadeV1

class FakeService:
    def __init__(self):
        self.calls = 0

    async def ticker(self, exchange, symbol):
        self.calls += 1
        return {"exchange": exchange, "symbol": symbol, "price": 100}

    async def order_book(self, exchange, symbol, limit=20):
        self.calls += 1
        return {"exchange": exchange, "symbol": symbol, "limit": limit}

@pytest.mark.asyncio
async def test_cached_market_facade_ticker_uses_cache():
    service = FakeService()
    facade = CachedMarketDataFacadeV1(service=service)
    first = await facade.ticker(SupportedExchange.BITUNIX, "BTC/USDT")
    second = await facade.ticker(SupportedExchange.BITUNIX, "BTC/USDT")
    assert first == second
    assert service.calls == 1
