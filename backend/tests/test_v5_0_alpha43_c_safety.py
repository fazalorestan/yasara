from app.platform_core.broker_layer.order_routing_safety import BrokerOrderRoutingSafetyPolicy

def test_v500_alpha43_c_safety(): assert BrokerOrderRoutingSafetyPolicy().policy()['paper_routing_only'] is True
