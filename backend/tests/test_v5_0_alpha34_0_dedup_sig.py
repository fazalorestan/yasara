from app.platform_core.auto_router_registry.dedup import AutoRouterDedupService

class R: path='/x'; methods={'GET'}
def test_v500_alpha34_0_dedup_sig(): assert AutoRouterDedupService().route_signature(R())[0]=='/x'