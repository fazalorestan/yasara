from app.v500_alpha44_build_intelligence.service import BuildIntelligenceFacadeV500Alpha44

def test_dashboard_ready(): assert BuildIntelligenceFacadeV500Alpha44().report()['dashboard_auto_update_ready'] is True
