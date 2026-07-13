from app.v500_alpha44_build_intelligence.service import BuildIntelligenceFacadeV500Alpha44

def test_no_real_broker(): assert BuildIntelligenceFacadeV500Alpha44().state_store()['real_broker_connection_enabled'] is False
