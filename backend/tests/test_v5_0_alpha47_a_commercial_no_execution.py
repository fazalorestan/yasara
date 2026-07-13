from app.v500_alpha47_build_pipeline.service import BuildPipelineFacadeV500Alpha47

def test_commercial_no_execution(): assert BuildPipelineFacadeV500Alpha47().report()['commercial_execution_engine_enabled'] is False
