from app.platform_core.production_runtime.enterprise.quality_score import RuntimeEnterpriseQualityScoreService

def test_quality(): assert RuntimeEnterpriseQualityScoreService().calculate()['ready'] is True
