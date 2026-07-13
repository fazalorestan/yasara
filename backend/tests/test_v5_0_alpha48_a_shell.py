from app.platform_core.windows_app.runtime_shell import WindowsRuntimeShellService

def test_shell(): assert WindowsRuntimeShellService().shell()['backend_process_required'] is True
