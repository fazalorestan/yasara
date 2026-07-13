from app.platform_core.live_data_pipeline.enterprise.runtime_acceptance import LiveDataEnterpriseRuntimeAcceptance

def test_v500_alpha39_e_runtime_manual(): assert LiveDataEnterpriseRuntimeAcceptance().contract()['manual_apply_required'] is False
