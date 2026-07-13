from app.platform_core.native_windows_launcher.readiness import NativeWindowsLauncherReadinessGate

def test_readiness(): assert NativeWindowsLauncherReadinessGate().run()['ready'] is True
