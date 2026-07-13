from app.v11_dashboard_runtime.snapshot_service import DashboardRuntimeServiceV11

def test_dashboard_snapshot_service():
    snapshot = DashboardRuntimeServiceV11().snapshot()
    assert snapshot.ready is True
    assert len(snapshot.panels) >= 3
