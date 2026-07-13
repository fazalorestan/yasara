from app.v500_alpha19_auto_router.service import AutoRouterFacadeV500Alpha19

def test_v500_alpha19_facade_readiness():
    assert 'score' in AutoRouterFacadeV500Alpha19().readiness()
