from app.v500_alpha21_patch_pipeline.models import PatchPipelineSummaryV500Alpha21

def test_v500_alpha21_summary():
    s=PatchPipelineSummaryV500Alpha21(); assert s.ready is True; assert s.v5_auto_discovery_enabled is True
