from app.platform_core.desktop_gui.ui_state import DesktopUIStateContract

def test_state(): assert DesktopUIStateContract().state()['persist_state'] is True
