class DesktopTabManager:
    def tabs(self):
        return {
            "ready": True,
            "tabs_enabled": True,
            "open_tabs": ["dashboard"],
            "default_tab": "dashboard",
            "closable_tabs": True,
            "hardcoded_dashboard": False,
        }

desktop_tab_manager = DesktopTabManager()
