from app.platform_core.broker_layer.health import BrokerHealthService

def test_v500_alpha37_a_health(): assert BrokerHealthService().health({'broker_id':'b','enabled':True})['status']=='ok'