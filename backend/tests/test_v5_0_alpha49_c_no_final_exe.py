from app.v500_alpha49_desktop_launcher.service import DesktopRuntimeLauncherFacadeV500Alpha49

def test_no_final_exe(): assert DesktopRuntimeLauncherFacadeV500Alpha49().summary().final_exe_generated is False
