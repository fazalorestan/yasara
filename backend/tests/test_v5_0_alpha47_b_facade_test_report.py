from app.v500_alpha47_ci_pipeline.service import CIPipelineFacadeV500Alpha47

def test_facade_test_report():
 r=CIPipelineFacadeV500Alpha47().test_report(); assert r is not None
