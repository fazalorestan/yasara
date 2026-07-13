from app.platform_core.broker_layer.broker_registry import BrokerRegistry

def test_v500_alpha43_a_broker_get(): assert BrokerRegistry().get('sim.broker')['ready'] is True
