from app.v500_alpha47_build_pipeline.service import BuildPipelineFacadeV500Alpha47

def test_no_real_broker(): assert BuildPipelineFacadeV500Alpha47().report()['real_broker_connection_enabled'] is False
