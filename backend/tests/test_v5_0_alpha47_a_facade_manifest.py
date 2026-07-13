from app.v500_alpha47_build_pipeline.service import BuildPipelineFacadeV500Alpha47

def test_facade_manifest():
 r=BuildPipelineFacadeV500Alpha47().manifest(); assert r is not None
