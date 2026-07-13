from app.platform_core.windows_portable_build.readiness import WindowsPortableBuildReadinessGate

def test_readiness(): assert WindowsPortableBuildReadinessGate().run()['ready'] is True
