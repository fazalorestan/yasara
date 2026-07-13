from app.platform_core.desktop_launcher.readiness import DesktopRuntimeLauncherReadinessGate

def test_readiness(): assert DesktopRuntimeLauncherReadinessGate().run()['ready'] is True
