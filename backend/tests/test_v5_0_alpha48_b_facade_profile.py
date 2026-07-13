from app.v500_alpha48_windows_packaging.service import WindowsPackagingFacadeV500Alpha48

def test_facade_profile():
 r=WindowsPackagingFacadeV500Alpha48().profile(); assert r is not None
