from app.v500_alpha49_native_desktop.service import NativeDesktopApplicationFacadeV500Alpha49

def test_no_final_exe(): assert NativeDesktopApplicationFacadeV500Alpha49().summary().final_exe_generated is False
