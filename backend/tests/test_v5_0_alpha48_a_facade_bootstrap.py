from app.v500_alpha48_windows_app.service import WindowsAppBootstrapFacadeV500Alpha48

def test_facade_bootstrap():
 r=WindowsAppBootstrapFacadeV500Alpha48().bootstrap(); assert r is not None
