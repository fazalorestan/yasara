from app.v500_alpha47_build_pipeline.service import BuildPipelineFacadeV500Alpha47

def test_facade_core():
 r=BuildPipelineFacadeV500Alpha47().core(); assert r is not None
