from app.v500_alpha47_ci_pipeline.service import CIPipelineFacadeV500Alpha47

def test_facade_core():
 r=CIPipelineFacadeV500Alpha47().core(); assert r is not None
