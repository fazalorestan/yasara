from app.platform_core.desktop_app.desktop_readiness import DesktopHostReadinessGate

def test_readiness(): assert DesktopHostReadinessGate().run()['ready'] is True
