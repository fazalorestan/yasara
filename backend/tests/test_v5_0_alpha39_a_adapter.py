from app.platform_core.live_data_pipeline.provider_adapter import LiveDataProviderAdapterContract

def test_v500_alpha39_a_adapter(): assert LiveDataProviderAdapterContract().adapter_contract()['real_provider_connection'] is False