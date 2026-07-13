from app.platform_core.live_data_pipeline.stream_recovery import LiveStreamRecoveryPolicy

def test_v500_alpha39_c_attempt(): assert LiveStreamRecoveryPolicy().attempt(0)['retry_allowed'] is True
