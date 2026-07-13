from app.platform_core.live_data_pipeline.data_safety import LiveDataSafetyPolicy

def test_v500_alpha39_a_validate_ok(): assert LiveDataSafetyPolicy().validate_snapshot({'source_id':'s','symbol':'BTCUSDT','price':1})['valid'] is True