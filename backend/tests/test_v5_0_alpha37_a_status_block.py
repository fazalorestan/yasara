from app.platform_core.broker_layer.service import BrokerLayerCoreService

def test_v500_alpha37_a_status_block(): assert BrokerLayerCoreService().status()['execution_allowed'] is False
