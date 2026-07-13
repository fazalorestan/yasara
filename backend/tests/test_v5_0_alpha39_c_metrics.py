from app.platform_core.live_data_pipeline.stream_metrics import LiveStreamMetricsService

def test_v500_alpha39_c_metrics(): assert LiveStreamMetricsService().metrics()['ready'] is True
