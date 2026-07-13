from app.platform_core.desktop_launcher.runtime_launcher import DesktopRuntimeLauncher

def test_launcher(): assert DesktopRuntimeLauncher().launcher()['final_exe_generated'] is False
