from app.platform_core.project_intelligence.state_sync_readiness import StateSyncReadinessGate

def test_readiness(): assert StateSyncReadinessGate().run()['ready'] is True
