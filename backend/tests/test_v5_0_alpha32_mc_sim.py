from app.platform_core.optimizer_pro.monte_carlo import MonteCarloRobustnessService

def test_v500_alpha32_mc_sim(): assert MonteCarloRobustnessService().simulate()['runs']==100