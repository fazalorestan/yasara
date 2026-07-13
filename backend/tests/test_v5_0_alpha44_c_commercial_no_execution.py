from app.v500_alpha44_build_intelligence.service import BuildIntelligenceFacadeV500Alpha44

def test_commercial_no_execution(): assert BuildIntelligenceFacadeV500Alpha44().build_metadata()['commercial_execution_engine_enabled'] is False
