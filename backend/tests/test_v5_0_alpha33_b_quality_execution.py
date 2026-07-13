from app.platform_core.ai_decision.quality_gate import AIDecisionQualityGate

def test_v500_alpha33_b_quality_execution(): assert AIDecisionQualityGate().evaluate({})['execution_allowed'] is False
