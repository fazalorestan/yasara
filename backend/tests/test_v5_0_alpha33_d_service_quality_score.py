from app.platform_core.ai_decision.enterprise.service import AIDecisionEnterpriseService

def test_v500_alpha33_d_service_quality_score():
 r=AIDecisionEnterpriseService().quality_score(); assert r is not None
