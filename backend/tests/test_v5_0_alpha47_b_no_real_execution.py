from app.v500_alpha47_ci_pipeline.service import CIPipelineFacadeV500Alpha47

def test_no_real_execution(): assert CIPipelineFacadeV500Alpha47().report()['real_execution_enabled'] is False
