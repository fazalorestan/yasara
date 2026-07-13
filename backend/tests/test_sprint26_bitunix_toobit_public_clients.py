import pytest
from app.multi_exchange_v1.adapters.bitunix import BitunixAdapterV1
from app.multi_exchange_v1.adapters.toobit import ToobitAdapterV1

class FakeClient:
    def __init__(self):
        self.calls = []

    async def get_json(self, url: str, params: dict | None = None):
        self.calls.append((url, params))
        if "depth" in url:
            return {"data": {"bids": [["100", "1"]], "asks": [["101", "2"]]}}
        return {"data": {"lastPrice": "100", "priceChangePercent": "1", "volume": "10"}}

@pytest.mark.asyncio
async def test_bitunix_ticker_uses_public_client():
    fake = FakeClient()
    adapter = BitunixAdapterV1(client=fake)
    ticker = await adapter.ticker("BTC/USDT")
    assert ticker.price == 100
    assert fake.calls[0][1]["symbol"] == "BTCUSDT"

@pytest.mark.asyncio
async def test_toobit_order_book_uses_public_client():
    fake = FakeClient()
    adapter = ToobitAdapterV1(client=fake)
    book = await adapter.order_book("BTC/USDT", limit=10)
    assert book.bids[0] == [100.0, 1.0]
    assert fake.calls[0][1]["limit"] == 10
