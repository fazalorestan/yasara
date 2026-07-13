from app.v500_alpha48_windows_app.service import WindowsAppBootstrapFacadeV500Alpha48

def test_facade_local_backend():
 r=WindowsAppBootstrapFacadeV500Alpha48().local_backend(); assert r is not None
