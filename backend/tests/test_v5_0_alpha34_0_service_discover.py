from app.platform_core.auto_router_registry.service import AutoRouterRegistryService

def test_v500_alpha34_0_service_discover(): assert AutoRouterRegistryService().discover()['ready'] is True