from app.platform_core.live_data_pipeline.data_safety import LiveDataSafetyPolicy

def test_v500_alpha39_a_validate_bad(): assert LiveDataSafetyPolicy().validate_snapshot({})['valid'] is False