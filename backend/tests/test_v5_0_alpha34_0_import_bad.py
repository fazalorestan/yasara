from app.platform_core.auto_router_registry.discovery import AutoRouterDiscovery

def test_v500_alpha34_0_import_bad(): assert AutoRouterDiscovery().import_module('app.api.v1.routes.nope')['ready'] is False