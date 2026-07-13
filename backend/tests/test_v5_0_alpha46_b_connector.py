from app.platform_core.desktop_app.live_dashboard_connector import DesktopLiveDashboardConnector

def test_connector(): assert DesktopLiveDashboardConnector().connect()['connected'] is True
