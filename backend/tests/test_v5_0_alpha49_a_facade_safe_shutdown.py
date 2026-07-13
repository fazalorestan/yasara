from app.v500_alpha49_native_desktop.service import NativeDesktopApplicationFacadeV500Alpha49

def test_facade_safe_shutdown():
 assert NativeDesktopApplicationFacadeV500Alpha49().safe_shutdown() is not None
