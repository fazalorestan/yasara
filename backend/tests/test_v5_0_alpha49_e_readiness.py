from app.platform_core.desktop_finalization.readiness import InternalDesktopBuildFinalizationReadinessGate

def test_readiness(): assert InternalDesktopBuildFinalizationReadinessGate().run()['ready'] is True
