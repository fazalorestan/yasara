from app.v500_alpha49_native_desktop.service import NativeDesktopApplicationFacadeV500Alpha49

def test_facade_summary():
 assert NativeDesktopApplicationFacadeV500Alpha49().summary() is not None
