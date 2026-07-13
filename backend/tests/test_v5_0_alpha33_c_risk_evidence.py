from app.platform_core.ai_decision.integration.risk_link import AIDecisionRiskLink

def test_v500_alpha33_c_risk_evidence(): assert AIDecisionRiskLink().evidence()['ready'] is True