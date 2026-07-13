from app.v500_alpha49_desktop_launcher.service import DesktopRuntimeLauncherFacadeV500Alpha49

def test_facade_build_readiness():
 assert DesktopRuntimeLauncherFacadeV500Alpha49().build_readiness() is not None
