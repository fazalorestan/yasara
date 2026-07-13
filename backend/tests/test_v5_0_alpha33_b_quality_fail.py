from app.platform_core.ai_decision.quality_gate import AIDecisionQualityGate

def test_v500_alpha33_b_quality_fail(): assert AIDecisionQualityGate().evaluate({'ready':True,'decision':{'confidence':10},'consensus':{'agreement_pct':80}})['passed'] is False
