from app.platform_core.live_data_pipeline.readiness import LiveDataPipelineCoreReadinessGate

def test_v500_alpha39_a_readiness(): assert LiveDataPipelineCoreReadinessGate().run()['ready'] is True