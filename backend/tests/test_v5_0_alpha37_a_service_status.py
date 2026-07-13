from app.platform_core.broker_layer.service import BrokerLayerCoreService

def test_v500_alpha37_a_service_status():
 r=BrokerLayerCoreService().status(); assert r is not None
