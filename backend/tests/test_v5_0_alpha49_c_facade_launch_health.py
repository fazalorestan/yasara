from app.v500_alpha49_desktop_launcher.service import DesktopRuntimeLauncherFacadeV500Alpha49

def test_facade_launch_health():
 assert DesktopRuntimeLauncherFacadeV500Alpha49().launch_health() is not None
