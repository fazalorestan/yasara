from app.v500_alpha24_runtime_api_smoke.models import RuntimeAPISmokeSummaryV500Alpha24

def test_v500_alpha24_summary():
    s=RuntimeAPISmokeSummaryV500Alpha24(); assert s.ready is True; assert s.smoke_test_enabled is True
