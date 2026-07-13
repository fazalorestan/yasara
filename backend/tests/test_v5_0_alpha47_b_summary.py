from app.v500_alpha47_ci_pipeline.models import CIPipelineSummaryV500Alpha47

def test_summary():
 s=CIPipelineSummaryV500Alpha47(); assert s.ready and s.test_pack_size==90 and s.build_id=='2026.47.B.001'
