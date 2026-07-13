from app.platform_core.api_routing.service import AutoRouterDiscoveryService

def test_v500_alpha19_service_swagger():
    assert AutoRouterDiscoveryService().swagger()['ready'] is True
