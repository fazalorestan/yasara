from app.v500_alpha48_windows_app.service import WindowsAppBootstrapFacadeV500Alpha48

def test_facade_exe_handoff():
 r=WindowsAppBootstrapFacadeV500Alpha48().exe_handoff(); assert r is not None
