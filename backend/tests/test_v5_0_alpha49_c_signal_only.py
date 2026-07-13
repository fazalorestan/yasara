from app.v500_alpha49_desktop_launcher.service import DesktopRuntimeLauncherFacadeV500Alpha49

def test_signal_only(): assert DesktopRuntimeLauncherFacadeV500Alpha49().summary().signal_only_mode is True
