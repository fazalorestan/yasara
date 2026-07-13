from app.platform_core.api_routing.health import AutoRouterHealthReport

def test_v500_alpha19_health():
    h=AutoRouterHealthReport().report(); assert 'manual_router_patch_required' in h; assert h['execution_allowed'] is False
