from app.platform_core.replay_engine.backtest_link import ReplayBacktestLinkService

def test_v500_alpha30_backtest_link(): assert ReplayBacktestLinkService().link()['execution_allowed'] is False
