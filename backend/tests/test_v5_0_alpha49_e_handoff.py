from app.platform_core.desktop_finalization.exe_handoff import FirstRealExeHandoffContract

def test_handoff(): assert FirstRealExeHandoffContract().contract()['ready'] is True
