from app.platform_core.ai_decision.integration.risk_link import AIDecisionRiskLink

def test_v500_alpha33_c_risk_check(): assert AIDecisionRiskLink().check()['execution_allowed'] is False