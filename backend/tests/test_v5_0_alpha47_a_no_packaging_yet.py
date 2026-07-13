from app.v500_alpha47_build_pipeline.service import BuildPipelineFacadeV500Alpha47

def test_no_packaging_yet(): assert BuildPipelineFacadeV500Alpha47().summary().packaging_enabled is False
