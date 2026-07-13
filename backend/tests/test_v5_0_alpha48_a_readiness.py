from app.platform_core.windows_app.readiness import WindowsAppBootstrapReadinessGate

def test_readiness(): assert WindowsAppBootstrapReadinessGate().run()['ready'] is True
