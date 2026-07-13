from app.v500_alpha47_build_pipeline.models import BuildPipelineSummaryV500Alpha47

def test_guard(): assert BuildPipelineSummaryV500Alpha47().ready is True
