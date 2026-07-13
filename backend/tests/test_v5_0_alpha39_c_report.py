from app.platform_core.live_data_pipeline.stream_report import LiveStreamManagerReport

def test_v500_alpha39_c_report(): assert LiveStreamManagerReport().report()['ready'] is True
