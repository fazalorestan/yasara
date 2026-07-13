class DesktopNavigationStateManager:
    def state(self):
        return {
            "ready": True,
            "current_route": "dashboard",
            "previous_route": None,
            "navigation_history_enabled": True,
            "can_go_back": False,
            "hardcoded_dashboard": False,
        }

desktop_navigation_state_manager = DesktopNavigationStateManager()
