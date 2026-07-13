from app.platform_core.native_desktop.readiness import NativeDesktopApplicationReadinessGate

def test_readiness(): assert NativeDesktopApplicationReadinessGate().run()['ready'] is True
