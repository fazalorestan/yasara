from app.v25_risk_backtest_paper.service import RiskBacktestPaperServiceV25
from app.v25_risk_backtest_paper.models import RiskRequestV25

def test_v25_risk():
    r = RiskBacktestPaperServiceV25().risk(RiskRequestV25())
    assert r["ready"] is True
    assert r["position_size"] > 0
    assert r["live_trading_enabled"] is False
