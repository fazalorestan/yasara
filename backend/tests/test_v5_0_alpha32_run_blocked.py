from app.platform_core.optimizer_pro.service import StrategyOptimizerProService

def test_v500_alpha32_run_blocked(): assert StrategyOptimizerProService().run()['execution_allowed'] is False
