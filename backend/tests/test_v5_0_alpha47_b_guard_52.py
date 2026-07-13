from app.v500_alpha47_ci_pipeline.models import CIPipelineSummaryV500Alpha47

def test_guard(): assert CIPipelineSummaryV500Alpha47().ready is True
