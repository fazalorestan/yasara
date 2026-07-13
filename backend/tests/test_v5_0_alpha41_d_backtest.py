from app.platform_core.strategy_engine.backtest_contract import StrategyBacktestContract

def test_v500_alpha41_d_backtest(): assert StrategyBacktestContract().contract()['execution_allowed'] is False
