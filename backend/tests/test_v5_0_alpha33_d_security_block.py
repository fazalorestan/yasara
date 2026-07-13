from app.platform_core.ai_decision.enterprise.security import AIDecisionSecurityGate

def test_v500_alpha33_d_security_block(): assert AIDecisionSecurityGate().evaluate()['execution_allowed'] is False