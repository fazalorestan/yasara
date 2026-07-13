from app.platform_core.desktop_app.dashboard_plugin_loader import DesktopDashboardPluginLoaderContract

def test_plugin(): assert DesktopDashboardPluginLoaderContract().contract()['plugin_loader_enabled'] is True
