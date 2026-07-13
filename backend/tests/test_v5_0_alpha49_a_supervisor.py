from app.platform_core.native_desktop.backend_supervisor import DesktopBackendProcessSupervisor

def test_supervisor(): assert DesktopBackendProcessSupervisor().policy()['fail_closed'] is True
