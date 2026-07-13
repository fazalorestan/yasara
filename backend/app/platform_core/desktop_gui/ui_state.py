class DesktopUIStateContract:
    def state(self):
        return {
            "ready": True,
            "active_route": "dashboard",
            "sidebar_collapsed": False,
            "theme": "system",
            "last_panel": "dashboard",
            "persist_state": True,
            "safe_to_restore": True,
        }

desktop_ui_state_contract = DesktopUIStateContract()
