from app.v34_market_analysis.service import MarketAnalysisEngineServiceV34

def test_v34_summary():
    s = MarketAnalysisEngineServiceV34().summary()
    assert s.product_progress_percent == 72
    assert s.constitution_compliant is True
