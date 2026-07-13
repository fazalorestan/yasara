from app.v500_alpha48_windows_packaging.service import WindowsPackagingFacadeV500Alpha48

def test_facade_layout():
 r=WindowsPackagingFacadeV500Alpha48().layout(); assert r is not None
