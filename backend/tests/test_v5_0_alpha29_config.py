from app.platform_core.backtest_engine.config import BacktestConfigService

def test_v500_alpha29_config(): assert BacktestConfigService().default()['initial_equity'] == 10000.0
