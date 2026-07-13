from app.platform_core.auto_router_lazy_service_registry.readiness import AutoRouterLazyServiceRegistryReadinessGate

def test_readiness():
    assert AutoRouterLazyServiceRegistryReadinessGate().run()["ready"] is True
