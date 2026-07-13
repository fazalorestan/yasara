from app.platform_core.ai_decision.quality_gate import AIDecisionQualityGate

def test_v500_alpha33_b_quality_pass(): assert AIDecisionQualityGate().evaluate({'ready':True,'decision':{'confidence':80},'consensus':{'agreement_pct':80}})['passed'] is True
