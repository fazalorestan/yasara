import pytest
from app.account_sync_v1.application.service import AccountSyncServiceV1

@pytest.mark.asyncio
async def test_stream_connect_and_ingest_order_update():
    service = AccountSyncServiceV1()
    state = await service.connect_stream("u1")
    assert state.status == "connected"
    event = await service.ingest_event("u1", {"e": "ORDER_TRADE_UPDATE", "o": {"s": "BTCUSDT"}})
    assert event.event_type == "order_update"
    history = await service.stream_history()
    assert len(history) == 1
