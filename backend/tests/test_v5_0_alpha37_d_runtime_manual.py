from app.platform_core.broker_layer.enterprise.runtime_acceptance import BrokerEnterpriseRuntimeAcceptance

def test_v500_alpha37_d_runtime_manual(): assert BrokerEnterpriseRuntimeAcceptance().contract()['manual_apply_required'] is False