from app.v500_alpha48_windows_packaging.service import WindowsPackagingFacadeV500Alpha48

def test_no_exe_packaging_yet(): assert WindowsPackagingFacadeV500Alpha48().summary().exe_packaging_enabled is False
