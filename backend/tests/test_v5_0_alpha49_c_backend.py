from app.platform_core.desktop_launcher.backend_launch_contract import BackendLaunchContract

def test_backend(): assert BackendLaunchContract().contract()['fail_closed_on_error'] is True
