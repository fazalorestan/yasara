from app.v11_risk_control.phase7_summary import V11Phase7SummaryBuilder

def test_v11_phase7_summary():
    summary = V11Phase7SummaryBuilder().build()
    assert summary.ready is True
    assert "guarded_paper_trading" in summary.capabilities
    assert summary.safety == "risk_guarded_paper_trading_only"
