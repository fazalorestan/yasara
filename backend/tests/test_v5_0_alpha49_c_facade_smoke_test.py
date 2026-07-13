from app.v500_alpha49_desktop_launcher.service import DesktopRuntimeLauncherFacadeV500Alpha49

def test_facade_smoke_test():
 assert DesktopRuntimeLauncherFacadeV500Alpha49().smoke_test() is not None
