from app.platform_core.optimizer_pro.service import StrategyOptimizerProService

def test_v500_alpha32_trials_count(): assert len(StrategyOptimizerProService().trials()['items'])==3
