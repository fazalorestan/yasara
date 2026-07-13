from app.v500_alpha49_native_desktop.service import NativeDesktopApplicationFacadeV500Alpha49

def test_facade_readiness():
 assert NativeDesktopApplicationFacadeV500Alpha49().readiness() is not None
