from app.v500_alpha19_auto_router.models import AutoRouterSummaryV500Alpha19

def test_v500_alpha19_summary():
    s=AutoRouterSummaryV500Alpha19(); assert s.ready is True; assert s.manual_router_patch_required is False
