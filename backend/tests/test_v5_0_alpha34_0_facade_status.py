from app.v500_alpha34_0_auto_router_registry.service import AutoRouterRegistryFacadeV500Alpha340

def test_v500_alpha34_0_facade_status(): assert AutoRouterRegistryFacadeV500Alpha340().status()['execution_allowed'] is False