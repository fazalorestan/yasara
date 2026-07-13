from app.platform_core.ai_decision.enterprise.quality_score import AIDecisionQualityScoreService

def test_v500_alpha33_d_quality_min(): assert AIDecisionQualityScoreService().calculate()['overall'] >= 9.5