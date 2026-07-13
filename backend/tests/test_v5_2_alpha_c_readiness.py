from app.platform_core.windows_spec_fix.readiness import WindowsSpecOutputFixReadinessGate

def test_readiness(): assert WindowsSpecOutputFixReadinessGate().run()['ready'] is True
