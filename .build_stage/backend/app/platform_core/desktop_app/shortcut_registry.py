class DesktopShortcutRegistry:
    def shortcuts(self):
        return {
            "ready": True,
            "shortcuts": {
                "refresh_dashboard": "Ctrl+R",
                "open_command_palette": "Ctrl+K",
                "open_settings": "Ctrl+,",
            },
            "count": 3,
            "dangerous_shortcuts_enabled": False,
            "real_execution_enabled": False,
        }

desktop_shortcut_registry = DesktopShortcutRegistry()
