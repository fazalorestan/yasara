import pytest
from app.multi_exchange_v1.domain.models import SupportedExchange
from app.multi_exchange_v1.snapshot import MarketSnapshotAggregatorV1

class FakeService:
    async def ticker(self, exchange, symbol):
        return {"price": 100, "change_percent": 1.5, "volume": 10}

@pytest.mark.asyncio
async def test_market_snapshot_aggregator():
    snapshot = await MarketSnapshotAggregatorV1().build(["BTC/USDT"], FakeService(), [SupportedExchange.BITUNIX, SupportedExchange.TOOBIT])
    assert len(snapshot.items) == 2
    assert snapshot.items[0].price == 100
