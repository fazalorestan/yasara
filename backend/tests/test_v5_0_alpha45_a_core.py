from app.platform_core.production_runtime.runtime_core import RuntimeCoreService

def test_core(): assert RuntimeCoreService().status()['bootable'] is True
