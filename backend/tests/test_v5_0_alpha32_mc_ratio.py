from app.platform_core.optimizer_pro.monte_carlo import MonteCarloRobustnessService

def test_v500_alpha32_mc_ratio():
 s=MonteCarloRobustnessService(); assert s.robustness_ratio(s.simulate())['ready'] is True