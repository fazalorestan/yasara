from app.v34_market_analysis.service import MarketAnalysisEngineServiceV34

def test_v34_timeframe():
    data = MarketAnalysisEngineServiceV34().analyze_timeframe("BTCUSDT", "binance", "1m", 60)
    assert data["timeframe"] == "1m"
    assert "trend" in data
    assert "regime" in data
