from app.platform_core.optimizer.ranking import OptimizerRankingService

def test_v500_alpha31_ranking(): assert OptimizerRankingService().rank([{'score':1},{'score':5}])['best']['score'] == 5
