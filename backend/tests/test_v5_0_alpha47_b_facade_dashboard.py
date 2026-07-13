from app.v500_alpha47_ci_pipeline.service import CIPipelineFacadeV500Alpha47

def test_facade_dashboard():
 r=CIPipelineFacadeV500Alpha47().dashboard(); assert r is not None
