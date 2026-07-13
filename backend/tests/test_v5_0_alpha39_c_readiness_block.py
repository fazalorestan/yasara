from app.platform_core.live_data_pipeline.stream_readiness import LiveStreamManagerReadinessGate

def test_v500_alpha39_c_readiness_block(): assert LiveStreamManagerReadinessGate().run()['execution_allowed'] is False
