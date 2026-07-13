from app.v500_alpha49_desktop_launcher.service import DesktopRuntimeLauncherFacadeV500Alpha49

def test_facade_backend_launch():
 assert DesktopRuntimeLauncherFacadeV500Alpha49().backend_launch() is not None
