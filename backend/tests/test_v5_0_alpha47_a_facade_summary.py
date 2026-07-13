from app.v500_alpha47_build_pipeline.service import BuildPipelineFacadeV500Alpha47

def test_facade_summary():
 r=BuildPipelineFacadeV500Alpha47().summary(); assert r is not None
