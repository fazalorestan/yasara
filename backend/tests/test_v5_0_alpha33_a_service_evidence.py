from app.platform_core.ai_decision.service import AIDecisionCoreService

def test_v500_alpha33_a_service_evidence(): assert len(AIDecisionCoreService().sample_evidence())==3
