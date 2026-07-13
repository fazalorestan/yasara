from app.v500_alpha49_desktop_launcher.service import DesktopRuntimeLauncherFacadeV500Alpha49

def test_facade_launcher():
 assert DesktopRuntimeLauncherFacadeV500Alpha49().launcher() is not None
