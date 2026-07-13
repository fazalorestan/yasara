from app.v500_alpha48_windows_app.service import WindowsAppBootstrapFacadeV500Alpha48

def test_facade_summary():
 r=WindowsAppBootstrapFacadeV500Alpha48().summary(); assert r is not None
