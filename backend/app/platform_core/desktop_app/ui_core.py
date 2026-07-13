class DesktopUICoreService:
    def status(self):
        return {
            "ready": True,
            "ui_core": "desktop_ui_framework",
            "mode": "development_shell",
            "connected_to_desktop_host": True,
            "hardcoded_dashboard": False,
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
        }

desktop_ui_core_service = DesktopUICoreService()
