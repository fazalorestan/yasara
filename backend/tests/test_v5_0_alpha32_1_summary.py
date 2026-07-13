from app.v500_alpha32_1_definitive_patch_runner.models import DefinitivePatchRunnerSummaryV500Alpha321

def test_v500_alpha32_1_summary():
 s=DefinitivePatchRunnerSummaryV500Alpha321(); assert s.ready and s.manual_router_patch_required_after_this is False
