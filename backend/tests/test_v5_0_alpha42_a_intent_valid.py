from app.platform_core.execution_engine.order_intent import OrderIntentService

def test_v500_alpha42_a_intent_valid():
 s=OrderIntentService(); assert s.validate(s.intent())['valid'] is True
