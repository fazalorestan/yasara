from app.platform_core.project_intelligence.pic_readiness import ProjectIntelligenceReadinessGate

def test_readiness(): assert ProjectIntelligenceReadinessGate().run()['ready'] is True
