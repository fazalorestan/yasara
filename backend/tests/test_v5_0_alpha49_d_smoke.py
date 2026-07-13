from app.platform_core.windows_portable_build.launch_smoke_contract import WindowsPortableLaunchSmokeContract

def test_smoke(): assert WindowsPortableLaunchSmokeContract().smoke()['ready'] is True
