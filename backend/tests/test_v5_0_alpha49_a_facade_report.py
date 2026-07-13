from app.v500_alpha49_native_desktop.service import NativeDesktopApplicationFacadeV500Alpha49

def test_facade_report():
 assert NativeDesktopApplicationFacadeV500Alpha49().report() is not None
