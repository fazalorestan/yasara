from app.platform_core.api_routing.discovery import AutoRouterDiscovery

def test_v500_alpha19_discovery_files():
    assert isinstance(AutoRouterDiscovery().discover_files(), list)
