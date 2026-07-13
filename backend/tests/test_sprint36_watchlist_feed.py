import pytest
from app.multi_exchange_v1.domain.models import SupportedExchange
from app.multi_exchange_v1.watchlist_feed import MultiExchangeWatchlistFeedV1, MultiExchangeWatchlistRequestV1

class FakeService:
    async def ticker(self, exchange, symbol):
        return {"price": 123}

@pytest.mark.asyncio
async def test_multi_exchange_watchlist_feed():
    request = MultiExchangeWatchlistRequestV1(symbols=["BTC/USDT"], preferred_exchange=SupportedExchange.TOOBIT)
    items = await MultiExchangeWatchlistFeedV1().build(request, FakeService())
    assert items[0].selected_exchange == SupportedExchange.TOOBIT
    assert items[0].price == 123
