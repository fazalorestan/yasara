from app.v500_alpha47_build_pipeline.service import BuildPipelineFacadeV500Alpha47

def test_facade_plugin_contract():
 r=BuildPipelineFacadeV500Alpha47().plugin_contract(); assert r is not None
