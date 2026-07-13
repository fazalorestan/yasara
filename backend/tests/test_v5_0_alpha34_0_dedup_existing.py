from app.platform_core.auto_router_registry.dedup import AutoRouterDedupService

class A: routes=[]
def test_v500_alpha34_0_dedup_existing(): assert AutoRouterDedupService().existing_signatures(A()) == set()