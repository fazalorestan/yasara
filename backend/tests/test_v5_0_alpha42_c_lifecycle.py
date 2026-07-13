from app.platform_core.execution_engine.order_lifecycle import OrderLifecycleService

def test_v500_alpha42_c_lifecycle(): assert OrderLifecycleService().lifecycle()['current_state']=='journaled'
