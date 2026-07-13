from app.v500_alpha44_build_intelligence.service import BuildIntelligenceFacadeV500Alpha44

def test_not_hardcoded(): assert BuildIntelligenceFacadeV500Alpha44().contract()['hardcoded_dashboard'] is False
