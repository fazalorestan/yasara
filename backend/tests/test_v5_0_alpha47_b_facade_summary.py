from app.v500_alpha47_ci_pipeline.service import CIPipelineFacadeV500Alpha47

def test_facade_summary():
 r=CIPipelineFacadeV500Alpha47().summary(); assert r is not None
