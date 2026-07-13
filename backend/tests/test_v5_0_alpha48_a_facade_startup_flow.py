from app.v500_alpha48_windows_app.service import WindowsAppBootstrapFacadeV500Alpha48

def test_facade_startup_flow():
 r=WindowsAppBootstrapFacadeV500Alpha48().startup_flow(); assert r is not None
