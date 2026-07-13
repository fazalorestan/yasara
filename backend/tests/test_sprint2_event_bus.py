import asyncio
import pytest
from app.market_data.domain.events import MarketEvent, MarketEventType
from app.market_data.infrastructure.event_bus import AsyncMarketEventBus

@pytest.mark.asyncio
async def test_event_bus_delivers_events():
    bus = AsyncMarketEventBus()
    received = []
    async def handler(event):
        received.append(event)
    bus.subscribe(MarketEventType.TICKER, handler)
    await bus.start()
    await bus.publish(MarketEvent(event_type=MarketEventType.TICKER, exchange="binance_futures", symbol="BTC/USDT", payload={"price": 1}))
    await asyncio.sleep(0.05)
    await bus.stop()
    assert len(received) == 1
    assert bus.published == 1
