from app.platform_core.desktop_app.ui_readiness import DesktopUIReadinessGate

def test_readiness(): assert DesktopUIReadinessGate().run()['ready'] is True
