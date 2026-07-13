from app.platform_core.broker_layer.enterprise.quality_score import BrokerEnterpriseQualityScoreService

def test_v500_alpha37_d_quality(): assert BrokerEnterpriseQualityScoreService().calculate()['ready'] is True