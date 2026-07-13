from app.v500_alpha47_ci_pipeline.service import CIPipelineFacadeV500Alpha47

def test_no_real_broker(): assert CIPipelineFacadeV500Alpha47().report()['real_broker_connection_enabled'] is False
