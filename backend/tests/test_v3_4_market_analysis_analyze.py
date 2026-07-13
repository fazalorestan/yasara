from app.v34_market_analysis.models import MarketAnalysisRequestV34
from app.v34_market_analysis.service import MarketAnalysisEngineServiceV34

def test_v34_analyze():
    data = MarketAnalysisEngineServiceV34().analyze(MarketAnalysisRequestV34(timeframes=["1m","5m"], limit=60))
    assert data["ready"] is True
    assert len(data["multi_timeframe"]) == 2
    assert data["constitution_compliant"] is True
    assert data["live_trading_enabled"] is False
