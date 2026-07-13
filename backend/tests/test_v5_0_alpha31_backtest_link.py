from app.platform_core.optimizer.backtest_link import OptimizerBacktestLinkService

def test_v500_alpha31_backtest_link(): assert OptimizerBacktestLinkService().link()['execution_allowed'] is False
