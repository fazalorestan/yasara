from app.platform_core.broker_layer.registry import BrokerRegistryService

def test_v500_alpha37_a_registry_register(): assert BrokerRegistryService().register({'broker_id':'x'})['registered'] is True