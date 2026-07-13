from app.v500_alpha34_0_auto_router_registry.service import AutoRouterRegistryFacadeV500Alpha340

def test_v500_alpha34_0_facade_discover(): assert AutoRouterRegistryFacadeV500Alpha340().discover()['ready'] is True