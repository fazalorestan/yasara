from app.platform_core.api_routing.discovery import AutoRouterDiscovery

def test_v500_alpha19_discovery_modules():
    assert isinstance(AutoRouterDiscovery().discover_modules(), list)
