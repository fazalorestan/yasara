from app.platform_core.desktop_gui.status_bar import DesktopStatusBarContract

def test_status(): assert DesktopStatusBarContract().status_bar()['shows_signal_only'] is True
