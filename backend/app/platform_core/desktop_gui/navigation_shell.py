class DesktopNavigationShellContract:
    def navigation(self):
        return {
            "ready": True,
            "items": ["dashboard", "runtime", "build", "ci", "health", "settings"],
            "default_item": "dashboard",
            "collapsible": True,
            "keyboard_navigation": True,
        }

desktop_navigation_shell_contract = DesktopNavigationShellContract()
