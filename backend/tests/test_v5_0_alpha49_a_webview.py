from app.platform_core.native_desktop.dashboard_webview_host import DashboardWebViewHost

def test_webview(): assert DashboardWebViewHost().configuration()['external_navigation_allowed'] is False
