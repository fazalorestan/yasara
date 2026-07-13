from app.platform_core.live_data_pipeline.provider_adapter import LiveDataProviderAdapterContract

def test_v500_alpha39_a_snapshot(): assert LiveDataProviderAdapterContract().simulated_snapshot()['price']==50000.0