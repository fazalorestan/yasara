from app.v500_alpha47_build_pipeline.service import BuildPipelineFacadeV500Alpha47

def test_facade_validation():
 r=BuildPipelineFacadeV500Alpha47().validation(); assert r is not None
