from app.v11_operations.phase5_summary import V11Phase5SummaryBuilder

def test_v11_phase5_summary():
    summary = V11Phase5SummaryBuilder().build()
    assert summary.ready is True
    assert "cleanup_project_bat" in summary.capabilities
    assert summary.safety == "maintenance_only_no_trading"
