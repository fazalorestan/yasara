from app.v11_paper_trading.phase6_summary import V11Phase6SummaryBuilder

def test_v11_phase6_summary():
    summary = V11Phase6SummaryBuilder().build()
    assert summary.ready is True
    assert "paper_order_manager" in summary.capabilities
    assert summary.safety == "paper_trading_only_no_live_orders"
