from app.platform_core.production_runtime.restart_lifecycle import RuntimeRestartLifecycleService

def test_restart(): assert RuntimeRestartLifecycleService().restart()['completed'] is True
