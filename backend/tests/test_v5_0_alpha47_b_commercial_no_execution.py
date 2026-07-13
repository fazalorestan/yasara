from app.v500_alpha47_ci_pipeline.service import CIPipelineFacadeV500Alpha47

def test_commercial_no_execution(): assert CIPipelineFacadeV500Alpha47().report()['commercial_execution_engine_enabled'] is False
