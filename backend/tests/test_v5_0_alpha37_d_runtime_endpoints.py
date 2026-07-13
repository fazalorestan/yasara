from app.platform_core.broker_layer.enterprise.runtime_acceptance import BrokerEnterpriseRuntimeAcceptance

def test_v500_alpha37_d_runtime_endpoints(): assert len(BrokerEnterpriseRuntimeAcceptance().contract()['required_runtime_endpoints']) == 4