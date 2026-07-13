from app.v500_alpha25_self_healing_patch_pipeline.models import SelfHealingPatchPipelineSummaryV500Alpha25

def test_v500_alpha25_summary():
    s=SelfHealingPatchPipelineSummaryV500Alpha25(); assert s.ready is True; assert s.auto_discovery_enabled is True
