from app.v500_alpha49_native_desktop.service import NativeDesktopApplicationFacadeV500Alpha49

def test_facade_contract():
 assert NativeDesktopApplicationFacadeV500Alpha49().contract() is not None
