from app.platform_core.production_runtime.shutdown_lifecycle import RuntimeShutdownLifecycleService

def test_shutdown(): assert RuntimeShutdownLifecycleService().shutdown()['completed'] is True
