from app.v500_alpha48_windows_packaging.service import WindowsPackagingFacadeV500Alpha48

def test_facade_summary():
 r=WindowsPackagingFacadeV500Alpha48().summary(); assert r is not None
