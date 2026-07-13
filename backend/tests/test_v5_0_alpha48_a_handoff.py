from app.platform_core.windows_app.exe_handoff_readiness import WindowsExeHandoffReadinessContract

def test_handoff(): assert WindowsExeHandoffReadinessContract().contract()['ready'] is True
