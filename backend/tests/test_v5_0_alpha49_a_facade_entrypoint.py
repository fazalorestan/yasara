from app.v500_alpha49_native_desktop.service import NativeDesktopApplicationFacadeV500Alpha49

def test_facade_entrypoint():
 assert NativeDesktopApplicationFacadeV500Alpha49().entrypoint() is not None
