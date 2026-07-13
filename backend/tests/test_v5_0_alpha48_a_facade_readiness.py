from app.v500_alpha48_windows_app.service import WindowsAppBootstrapFacadeV500Alpha48

def test_facade_readiness():
 r=WindowsAppBootstrapFacadeV500Alpha48().readiness(); assert r is not None
