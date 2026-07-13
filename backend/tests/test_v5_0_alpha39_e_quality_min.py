from app.platform_core.live_data_pipeline.enterprise.quality_score import LiveDataEnterpriseQualityScoreService

def test_v500_alpha39_e_quality_min(): assert LiveDataEnterpriseQualityScoreService().calculate()['overall'] >= 9.5
