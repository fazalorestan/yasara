from app.v11_ai_market_intelligence.phase3_summary import V11Phase3SummaryBuilder

def test_v11_phase3_summary():
    summary = V11Phase3SummaryBuilder().build()
    assert summary.ready is True
    assert "signal_scorer" in summary.capabilities
    assert summary.safety == "analysis_only_no_live_trading"
