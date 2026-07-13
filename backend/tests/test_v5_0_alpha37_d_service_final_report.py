from app.platform_core.broker_layer.enterprise.service import BrokerEnterpriseService

def test_v500_alpha37_d_service_final_report():
 r=BrokerEnterpriseService().final_report(); assert r is not None
