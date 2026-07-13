from app.platform_core.execution_engine.order_intent import OrderIntentService

def test_v500_alpha42_a_intent(): assert OrderIntentService().intent()['side']=='hold'
