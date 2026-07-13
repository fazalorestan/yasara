from app.platform_core.ai_decision.enterprise.quality_score import AIDecisionQualityScoreService

def test_v500_alpha33_d_quality(): assert AIDecisionQualityScoreService().calculate()['ready'] is True