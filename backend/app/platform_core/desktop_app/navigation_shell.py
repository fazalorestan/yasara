class DesktopNavigationShell:
    def navigation(self):
        return {"ready": True, "routes": ["dashboard", "project", "runtime", "settings"], "default_route": "dashboard", "dashboard_route_enabled": True, "hardcoded_dashboard": False}
desktop_navigation_shell = DesktopNavigationShell()
