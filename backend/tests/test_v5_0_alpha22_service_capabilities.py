from app.platform_core.broker.service import BrokerLayerFoundationService

def test_v500_alpha22_service_capabilities(): assert BrokerLayerFoundationService().capabilities()['ready'] is True
