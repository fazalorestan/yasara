from app.v500_alpha49_desktop_launcher.service import DesktopRuntimeLauncherFacadeV500Alpha49

def test_auto_trading_off(): assert DesktopRuntimeLauncherFacadeV500Alpha49().summary().auto_trading_enabled is False
