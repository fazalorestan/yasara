from app.v500_alpha29_backtest_engine.models import BacktestEngineSummaryV500Alpha29

def test_v500_alpha29_summary():
    s=BacktestEngineSummaryV500Alpha29(); assert s.ready is True; assert s.real_execution_enabled is False
