from app.platform_core.broker_layer.service import BrokerLayerCoreService

def test_v500_alpha37_a_service_default_broker():
 r=BrokerLayerCoreService().default_broker(); assert r is not None
