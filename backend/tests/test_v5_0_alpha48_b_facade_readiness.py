from app.v500_alpha48_windows_packaging.service import WindowsPackagingFacadeV500Alpha48

def test_facade_readiness():
 r=WindowsPackagingFacadeV500Alpha48().readiness(); assert r is not None
