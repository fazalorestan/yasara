from app.platform_core.windows_packaging_enablement.readiness import GuardedPackagingReadinessGate

def test_readiness(): assert GuardedPackagingReadinessGate().run()['ready'] is True
