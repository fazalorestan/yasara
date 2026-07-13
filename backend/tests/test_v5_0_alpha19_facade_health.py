from app.v500_alpha19_auto_router.service import AutoRouterFacadeV500Alpha19

def test_v500_alpha19_facade_health():
    assert 'manual_router_patch_required' in AutoRouterFacadeV500Alpha19().health()
