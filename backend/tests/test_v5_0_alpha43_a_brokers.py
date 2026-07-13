from app.platform_core.broker_layer.broker_registry import BrokerRegistry

def test_v500_alpha43_a_brokers(): assert BrokerRegistry().list_brokers()['count']==2
