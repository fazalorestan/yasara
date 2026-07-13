from app.platform_core.execution_engine.execution_safety import ExecutionSafetyPolicy

def test_v500_alpha42_a_real_order_block(): assert ExecutionSafetyPolicy().can_execute_real_order()['allowed'] is False
