from app.platform_core.auto_router_registry.discovery import AutoRouterDiscovery

def test_v500_alpha34_0_import_ok(): assert AutoRouterDiscovery().import_module('app.api.v1.routes.v500_alpha34_0_auto_router_registry_v1')['has_router'] is True