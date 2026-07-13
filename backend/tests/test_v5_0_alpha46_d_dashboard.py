from app.platform_core.desktop_app.dashboard_center import DesktopLiveDashboardCenter

def test_dashboard(): assert DesktopLiveDashboardCenter().dashboard()['source']=='live_dashboard_backend'
