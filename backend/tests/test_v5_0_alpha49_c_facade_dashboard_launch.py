from app.v500_alpha49_desktop_launcher.service import DesktopRuntimeLauncherFacadeV500Alpha49

def test_facade_dashboard_launch():
 assert DesktopRuntimeLauncherFacadeV500Alpha49().dashboard_launch() is not None
