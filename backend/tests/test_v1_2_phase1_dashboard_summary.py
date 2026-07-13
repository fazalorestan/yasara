from app.v12_dashboard.service import DashboardShellServiceV12

def test_dashboard_shell_summary():
    summary = DashboardShellServiceV12().summary()
    assert summary.ready is True
    assert summary.progress_percent == 20
    assert summary.route == "/app"
