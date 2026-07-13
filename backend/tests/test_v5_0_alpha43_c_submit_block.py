from app.platform_core.broker_layer.order_routing_safety import BrokerOrderRoutingSafetyPolicy

def test_v500_alpha43_c_submit_block(): assert BrokerOrderRoutingSafetyPolicy().can_submit_real_order()['allowed'] is False
