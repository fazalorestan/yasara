from app.platform_core.optimizer.ranking import OptimizerRankingService

def test_v500_alpha31_ranking_empty(): assert OptimizerRankingService().rank([])['best'] is None
