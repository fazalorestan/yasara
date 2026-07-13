from app.platform_core.broker_layer.registry import BrokerRegistryService

def test_v500_alpha37_a_registry_list(): assert BrokerRegistryService().list_brokers()['count'] == 2