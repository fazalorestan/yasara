from app.platform_core.broker_layer.service import BrokerLayerCoreService

def test_v500_alpha37_a_service_health():
 r=BrokerLayerCoreService().health(); assert r is not None
