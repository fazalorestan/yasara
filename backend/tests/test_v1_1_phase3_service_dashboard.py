from app.v11_ai_market_intelligence.service import AIMarketIntelligenceServiceV11

def test_ai_market_intelligence_dashboard():
    payload = AIMarketIntelligenceServiceV11().dashboard_payload()
    assert payload["ready"] is True
    assert payload["count"] >= 1
    assert payload["safety"] == "analysis_only_no_trade_execution"
