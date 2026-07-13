class DesktopCommandPaletteContract:
    def contract(self):
        return {
            "ready": True,
            "command_palette_enabled": True,
            "commands": ["open_dashboard", "refresh_dashboard", "open_runtime", "open_settings"],
            "dangerous_commands_enabled": False,
            "real_execution_enabled": False,
        }

desktop_command_palette_contract = DesktopCommandPaletteContract()
