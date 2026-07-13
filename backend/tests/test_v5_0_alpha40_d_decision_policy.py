from app.platform_core.ai_intelligence.decision_policy import AIDecisionPolicyService

def test_v500_alpha40_d_decision_policy(): assert AIDecisionPolicyService().policy()['decision_mode']=='advisory_only'
