from app.platform_core.execution_engine.routing_safety import OrderRoutingSafetyPolicy

def test_v500_alpha42_b_safety(): assert OrderRoutingSafetyPolicy().policy()['routing_only'] is True
