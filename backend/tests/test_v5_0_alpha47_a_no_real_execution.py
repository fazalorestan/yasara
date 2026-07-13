from app.v500_alpha47_build_pipeline.service import BuildPipelineFacadeV500Alpha47

def test_no_real_execution(): assert BuildPipelineFacadeV500Alpha47().report()['real_execution_enabled'] is False
