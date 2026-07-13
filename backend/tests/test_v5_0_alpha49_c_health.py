from app.platform_core.desktop_launcher.launch_health import DesktopLaunchHealthProvider

def test_health(): assert DesktopLaunchHealthProvider().health()['launch_health']=='green'
