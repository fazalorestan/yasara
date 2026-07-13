from app.platform_core.auto_router_registry.discovery import AutoRouterDiscovery

def test_v500_alpha34_0_discover_type(): assert isinstance(AutoRouterDiscovery().discover_modules(), list)