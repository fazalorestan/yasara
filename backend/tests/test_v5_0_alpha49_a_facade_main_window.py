from app.v500_alpha49_native_desktop.service import NativeDesktopApplicationFacadeV500Alpha49

def test_facade_main_window():
 assert NativeDesktopApplicationFacadeV500Alpha49().main_window() is not None
