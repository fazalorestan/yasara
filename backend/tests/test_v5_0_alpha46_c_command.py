from app.platform_core.desktop_app.command_palette import DesktopCommandPaletteContract

def test_command(): assert DesktopCommandPaletteContract().contract()['dangerous_commands_enabled'] is False
