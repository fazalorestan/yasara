from app.platform_core.desktop_app.foundation_readiness import DesktopFoundationReadinessGate

def test_readiness(): assert DesktopFoundationReadinessGate().run()["ready"] is True
