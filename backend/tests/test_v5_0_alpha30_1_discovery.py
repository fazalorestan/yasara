from app.platform_core.router_auto_registration.discovery import RouteModuleDiscovery

def test_v500_alpha30_1_discovery(): assert isinstance(RouteModuleDiscovery().discover(), list)
