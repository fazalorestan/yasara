import pytest
from app.multi_exchange_v1.adapters.toobit import ToobitAdapterV1
from tests.helpers.fake_exchange_client import FakeExchangePublicClient

@pytest.mark.asyncio
async def test_toobit_ticker_scaffold_offline():
    fake = FakeExchangePublicClient()
    result = await ToobitAdapterV1(client=fake).ticker("ETH/USDT")
    assert result.exchange == "toobit"
    assert result.symbol == "ETH/USDT"
    assert result.price == 100
    assert fake.calls[0][1]["symbol"] == "ETHUSDT"
