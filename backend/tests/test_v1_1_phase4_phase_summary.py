from app.v11_dashboard_runtime.phase4_summary import V11Phase4SummaryBuilder

def test_v11_phase4_summary():
    summary = V11Phase4SummaryBuilder().build()
    assert summary.ready is True
    assert "unified_dashboard_snapshot_api" in summary.capabilities
    assert summary.safety == "dashboard_read_only_no_order_execution"
