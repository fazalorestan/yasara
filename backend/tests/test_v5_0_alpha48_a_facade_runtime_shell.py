from app.v500_alpha48_windows_app.service import WindowsAppBootstrapFacadeV500Alpha48

def test_facade_runtime_shell():
 r=WindowsAppBootstrapFacadeV500Alpha48().runtime_shell(); assert r is not None
