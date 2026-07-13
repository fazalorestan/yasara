from app.platform_core.strategy_engine.enterprise.quality_score import StrategyEnterpriseQualityScoreService

def test_v500_alpha41_e_quality(): assert StrategyEnterpriseQualityScoreService().calculate()['ready'] is True
