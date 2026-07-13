from app.v500_alpha33_1_simple_patch_runner.models import SimplePatchRunnerSummaryV500Alpha331

def test_v500_alpha33_1_summary():
 s=SimplePatchRunnerSummaryV500Alpha331(); assert s.ready and s.manual_router_patch_required_after_this is False
