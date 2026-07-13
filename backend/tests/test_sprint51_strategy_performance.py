from app.productivity_v1.strategy_performance import StrategyPerformanceEngineV1, StrategyTradeResultV1

def test_strategy_performance_win_rate():
    trades = [StrategyTradeResultV1(strategy_id="s1", pnl=10), StrategyTradeResultV1(strategy_id="s1", pnl=-5)]
    result = StrategyPerformanceEngineV1().analyze("s1", trades)
    assert result.win_rate == 50
    assert result.total_pnl == 5
