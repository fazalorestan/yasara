from app.v500_alpha47_ci_pipeline.service import CIPipelineFacadeV500Alpha47

def test_facade_readiness():
 r=CIPipelineFacadeV500Alpha47().readiness(); assert r is not None
