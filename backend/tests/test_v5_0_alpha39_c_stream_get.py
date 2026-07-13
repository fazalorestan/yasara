from app.platform_core.live_data_pipeline.stream_registry import LiveStreamRegistry

def test_v500_alpha39_c_stream_get(): assert LiveStreamRegistry().get('ticker.BTCUSDT')['ready'] is True
