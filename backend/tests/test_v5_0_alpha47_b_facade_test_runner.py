from app.v500_alpha47_ci_pipeline.service import CIPipelineFacadeV500Alpha47

def test_facade_test_runner():
 r=CIPipelineFacadeV500Alpha47().test_runner(); assert r is not None
