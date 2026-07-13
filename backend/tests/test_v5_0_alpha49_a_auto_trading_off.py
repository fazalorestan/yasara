from app.v500_alpha49_native_desktop.service import NativeDesktopApplicationFacadeV500Alpha49

def test_auto_trading_off(): assert NativeDesktopApplicationFacadeV500Alpha49().summary().auto_trading_enabled is False
