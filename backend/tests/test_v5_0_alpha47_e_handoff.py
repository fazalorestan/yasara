from app.platform_core.production_readiness.windows_exe_handoff import WindowsExecutableHandoffContract

def test_handoff(): assert WindowsExecutableHandoffContract().contract()['ready'] is True
