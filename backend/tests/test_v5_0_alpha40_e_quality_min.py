from app.platform_core.ai_intelligence.enterprise.quality_score import AIEnterpriseQualityScoreService

def test_v500_alpha40_e_quality_min(): assert AIEnterpriseQualityScoreService().calculate()['overall'] >= 9.5
