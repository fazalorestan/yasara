from app.platform_core.native_desktop.safe_shutdown import DesktopSafeShutdownController

def test_shutdown(): assert DesktopSafeShutdownController().policy()['force_signal_only'] is True
