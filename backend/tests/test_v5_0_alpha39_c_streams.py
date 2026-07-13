from app.platform_core.live_data_pipeline.stream_registry import LiveStreamRegistry

def test_v500_alpha39_c_streams(): assert LiveStreamRegistry().list_streams()['count']==3
