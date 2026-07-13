from app.platform_core.windows_exe_smoke_build.launch_smoke import WindowsExeLaunchSmokeContract

def test_smoke(): assert WindowsExeLaunchSmokeContract().smoke()['signal_only_mode'] is True
