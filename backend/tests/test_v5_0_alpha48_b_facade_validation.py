from app.v500_alpha48_windows_packaging.service import WindowsPackagingFacadeV500Alpha48

def test_facade_validation():
 r=WindowsPackagingFacadeV500Alpha48().validation(); assert r is not None
