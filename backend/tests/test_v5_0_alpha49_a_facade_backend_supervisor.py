from app.v500_alpha49_native_desktop.service import NativeDesktopApplicationFacadeV500Alpha49

def test_facade_backend_supervisor():
 assert NativeDesktopApplicationFacadeV500Alpha49().backend_supervisor() is not None
