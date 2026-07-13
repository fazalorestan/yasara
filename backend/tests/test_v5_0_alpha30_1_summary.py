from app.v500_alpha30_1_router_auto_registration.models import RouterAutoRegistrationSummaryV500Alpha301

def test_v500_alpha30_1_summary():
    s=RouterAutoRegistrationSummaryV500Alpha301(); assert s.ready is True; assert s.manual_router_patch_required is False
