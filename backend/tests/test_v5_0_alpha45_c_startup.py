from app.platform_core.production_runtime.startup_lifecycle import RuntimeStartupLifecycleService

def test_startup(): assert RuntimeStartupLifecycleService().startup()['completed'] is True
