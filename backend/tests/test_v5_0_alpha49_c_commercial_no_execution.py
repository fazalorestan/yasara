from app.v500_alpha49_desktop_launcher.service import DesktopRuntimeLauncherFacadeV500Alpha49

def test_commercial_no_execution(): assert DesktopRuntimeLauncherFacadeV500Alpha49().report()['commercial_execution_engine_enabled'] is False
