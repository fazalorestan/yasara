from app.platform_core.ai_intelligence.decision_policy import AIDecisionPolicyService

def test_v500_alpha40_d_can_decide(): assert AIDecisionPolicyService().can_decide()['allowed'] is False
