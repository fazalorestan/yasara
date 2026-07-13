from app.platform_core.ai_decision.enterprise.service import AIDecisionEnterpriseService

def test_v500_alpha33_d_final_status_score(): assert AIDecisionEnterpriseService().final_status()['quality_score'] >= 9.5
