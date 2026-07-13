from app.connectivity_v1.stream_manager import MultiStreamManagerV1, StreamSubscriptionV1, StreamType

def test_stream_manager_subscribe_unsubscribe():
    manager = MultiStreamManagerV1()
    manager.subscribe(StreamSubscriptionV1(stream_id="s1", exchange="bitunix", symbol="BTC/USDT", stream_type=StreamType.TICKER))
    assert len(manager.active()) == 1
    assert manager.unsubscribe("s1") is True
    assert len(manager.active()) == 0
