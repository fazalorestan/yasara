from app.platform_core.live_data_pipeline.enterprise.runtime_acceptance import LiveDataEnterpriseRuntimeAcceptance

def test_v500_alpha39_e_runtime_endpoints(): assert len(LiveDataEnterpriseRuntimeAcceptance().contract()['required_runtime_endpoints']) == 4
