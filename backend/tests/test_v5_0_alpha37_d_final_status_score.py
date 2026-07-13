from app.platform_core.broker_layer.enterprise.service import BrokerEnterpriseService

def test_v500_alpha37_d_final_status_score(): assert BrokerEnterpriseService().final_status()['quality_score'] >= 9.5
