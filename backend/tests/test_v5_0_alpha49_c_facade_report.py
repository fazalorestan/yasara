from app.v500_alpha49_desktop_launcher.service import DesktopRuntimeLauncherFacadeV500Alpha49

def test_facade_report():
 assert DesktopRuntimeLauncherFacadeV500Alpha49().report() is not None
