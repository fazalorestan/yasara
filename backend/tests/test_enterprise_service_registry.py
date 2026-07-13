from app.enterprise_v1.service_registry import ServiceDescriptorV1, ServiceRegistryV1

def test_service_registry():
    registry = ServiceRegistryV1()
    registry.register(ServiceDescriptorV1(name="api", module="app"))
    assert registry.healthy_services()[0].name == "api"
