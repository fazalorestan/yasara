from app.connectivity_v1.stream_manager import StreamType
from app.connectivity_v1.unified_streaming import UnifiedStreamingAPIServiceV1, UnifiedStreamRequestV1

def test_unified_streaming_subscribe_many():
    service = UnifiedStreamingAPIServiceV1()
    subs = service.subscribe_many(UnifiedStreamRequestV1(exchange="bitunix", symbols=["BTC/USDT", "ETH/USDT"], stream_type=StreamType.TICKER))
    assert len(subs) == 2
    assert len(service.manager.active()) == 2
