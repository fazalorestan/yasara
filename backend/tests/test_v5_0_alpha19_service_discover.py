from app.platform_core.api_routing.service import AutoRouterDiscoveryService

def test_v500_alpha19_service_discover():
    assert AutoRouterDiscoveryService().discover()['ready'] is True
