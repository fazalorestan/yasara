from app.v500_alpha49_native_desktop.service import NativeDesktopApplicationFacadeV500Alpha49

def test_facade_single_instance():
 assert NativeDesktopApplicationFacadeV500Alpha49().single_instance() is not None
