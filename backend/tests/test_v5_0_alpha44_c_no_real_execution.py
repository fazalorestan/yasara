from app.v500_alpha44_build_intelligence.service import BuildIntelligenceFacadeV500Alpha44

def test_no_real_execution(): assert BuildIntelligenceFacadeV500Alpha44().state_store()['real_execution_enabled'] is False
