from app.platform_core.auto_router_registry.discovery import AutoRouterDiscovery

def test_v500_alpha34_0_discover_routes(): assert any('v500_alpha' in x for x in AutoRouterDiscovery().discover_modules())