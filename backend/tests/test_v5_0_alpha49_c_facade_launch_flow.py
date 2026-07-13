from app.v500_alpha49_desktop_launcher.service import DesktopRuntimeLauncherFacadeV500Alpha49

def test_facade_launch_flow():
 assert DesktopRuntimeLauncherFacadeV500Alpha49().launch_flow() is not None
