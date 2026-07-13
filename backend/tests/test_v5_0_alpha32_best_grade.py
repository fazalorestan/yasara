from app.platform_core.optimizer_pro.service import StrategyOptimizerProService

def test_v500_alpha32_best_grade(): assert StrategyOptimizerProService().best()['robustness_grade'] in ['A','B','C','D']
