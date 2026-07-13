from app.platform_core.production_runtime.service_health import RuntimeServiceHealthContract

def test_health(): assert RuntimeServiceHealthContract().health()['services_healthy'] is True
