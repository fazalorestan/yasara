from app.v11_dashboard_runtime.snapshot_service import DashboardRuntimeServiceV11

def test_dashboard_summary_service():
    summary = DashboardRuntimeServiceV11().summary()
    assert summary.ready is True
    assert summary.panel_count >= 3
    assert "market_snapshot" in summary.sources
