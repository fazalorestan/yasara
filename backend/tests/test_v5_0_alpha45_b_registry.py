from app.platform_core.production_runtime.service_registry import RuntimeServiceRegistry

def test_registry(): assert RuntimeServiceRegistry().services()['count']==5
