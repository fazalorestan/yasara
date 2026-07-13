from app.v500_alpha47_build_pipeline.models import BuildPipelineSummaryV500Alpha47

def test_summary():
 s=BuildPipelineSummaryV500Alpha47(); assert s.ready and s.test_pack_size==90 and s.build_id=='2026.47.A.001'
