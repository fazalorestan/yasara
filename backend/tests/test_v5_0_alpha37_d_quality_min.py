from app.platform_core.broker_layer.enterprise.quality_score import BrokerEnterpriseQualityScoreService

def test_v500_alpha37_d_quality_min(): assert BrokerEnterpriseQualityScoreService().calculate()['overall'] >= 9.5