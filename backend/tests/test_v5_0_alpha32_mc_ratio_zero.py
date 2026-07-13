from app.platform_core.optimizer_pro.monte_carlo import MonteCarloRobustnessService

def test_v500_alpha32_mc_ratio_zero(): assert MonteCarloRobustnessService().robustness_ratio({'max_pnl':0})['ready'] is False