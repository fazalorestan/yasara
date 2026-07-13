from app.platform_core.broker_layer.registry import BrokerRegistryService

def test_v500_alpha37_a_registry_missing(): assert BrokerRegistryService().get('missing')['ready'] is False