from app.v11_exchange_connectivity.phase2_summary import V11Phase2SummaryBuilder

def test_v11_phase2_summary():
    summary = V11Phase2SummaryBuilder().build()
    assert summary.ready is True
    assert "safety_guard" in summary.capabilities
    assert summary.safety == "read_only_connectivity_no_live_trading"
