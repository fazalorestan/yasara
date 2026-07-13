from app.platform_core.desktop_app.sidebar_navigation import DesktopSidebarNavigation

def test_sidebar(): assert DesktopSidebarNavigation().sidebar()['dashboard_enabled'] is True
