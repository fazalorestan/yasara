from app.platform_core.production_runtime.resource_monitor import RuntimeResourceMonitor

def test_resources(): assert RuntimeResourceMonitor().snapshot()['within_limits'] is True
