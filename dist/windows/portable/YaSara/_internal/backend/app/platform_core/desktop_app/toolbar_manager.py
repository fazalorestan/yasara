class DesktopToolbarManager:
    def toolbar(self):
        return {
            "ready": True,
            "actions": ["refresh_dashboard", "run_tests", "open_settings"],
            "refresh_dashboard_action": True,
            "dangerous_actions_enabled": False,
            "real_execution_enabled": False,
        }

desktop_toolbar_manager = DesktopToolbarManager()
