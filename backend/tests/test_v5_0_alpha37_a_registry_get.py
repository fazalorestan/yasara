from app.platform_core.broker_layer.registry import BrokerRegistryService

def test_v500_alpha37_a_registry_get(): assert BrokerRegistryService().get('paper.demo')['ready'] is True