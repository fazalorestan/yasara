from app.platform_core.live_data_pipeline.data_safety import LiveDataSafetyPolicy

def test_v500_alpha39_a_safety(): assert LiveDataSafetyPolicy().policy()['read_only'] is True