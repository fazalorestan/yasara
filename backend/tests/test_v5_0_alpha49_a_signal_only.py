from app.v500_alpha49_native_desktop.service import NativeDesktopApplicationFacadeV500Alpha49

def test_signal_only(): assert NativeDesktopApplicationFacadeV500Alpha49().summary().signal_only_mode is True
