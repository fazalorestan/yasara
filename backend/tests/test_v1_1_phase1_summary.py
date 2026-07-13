from app.v11_market_data.phase1_summary import V11Phase1SummaryBuilder

def test_v11_phase1_summary():
    summary = V11Phase1SummaryBuilder().build()
    assert summary.ready is True
    assert "market_cache" in summary.capabilities
    assert summary.safety == "read_only_market_data_no_live_trading"
