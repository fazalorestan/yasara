from app.v500_alpha47_ci_pipeline.service import CIPipelineFacadeV500Alpha47

def test_facade_contract():
 r=CIPipelineFacadeV500Alpha47().contract(); assert r is not None
