class DesktopSidebarNavigation:
    def sidebar(self):
        return {
            "ready": True,
            "items": ["dashboard", "project", "runtime", "settings"],
            "default_item": "dashboard",
            "collapsible": True,
            "dashboard_enabled": True,
            "hardcoded_dashboard": False,
        }

desktop_sidebar_navigation = DesktopSidebarNavigation()
