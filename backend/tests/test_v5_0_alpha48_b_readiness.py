from app.platform_core.windows_packaging.readiness import WindowsPackagingReadinessGate

def test_readiness(): assert WindowsPackagingReadinessGate().run()['ready'] is True
