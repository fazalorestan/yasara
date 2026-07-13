from app.platform_core.ai_decision.events import AIDecisionEventBuilder

def test_v500_alpha33_a_event(): assert AIDecisionEventBuilder().build('x',{})['ready'] is True
