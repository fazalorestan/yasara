from app.platform_core.desktop_app.dashboard_widget_registry import DesktopDashboardWidgetRegistry

def test_widgets(): assert DesktopDashboardWidgetRegistry().widgets()['plugin_based'] is True
