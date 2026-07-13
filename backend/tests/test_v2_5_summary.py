from app.v25_risk_backtest_paper.service import RiskBacktestPaperServiceV25

def test_v25_summary():
    s = RiskBacktestPaperServiceV25().summary()
    assert s.operational_progress_percent == 98
    assert s.remaining_to_full_operational_percent == 2
