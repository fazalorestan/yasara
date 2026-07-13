from app.platform_core.execution_engine.routing_safety import OrderRoutingSafetyPolicy

def test_v500_alpha42_b_broker_block(): assert OrderRoutingSafetyPolicy().can_route_to_real_broker()['allowed'] is False
