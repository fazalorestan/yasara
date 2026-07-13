from app.v25_risk_backtest_paper.service import RiskBacktestPaperServiceV25

def test_v25_backtest():
    b = RiskBacktestPaperServiceV25().backtest()
    assert b["ready"] is True
    assert b["trades"] > 0
    assert b["live_trading_enabled"] is False
