from app.platform_core.ai_decision.service import AIDecisionCoreService

def test_v500_alpha33_a_service_confidence(): assert AIDecisionCoreService().confidence()['ready'] is True
