from app.v500_alpha49_native_desktop.service import NativeDesktopApplicationFacadeV500Alpha49

def test_no_real_execution(): assert NativeDesktopApplicationFacadeV500Alpha49().report()['real_execution_enabled'] is False
