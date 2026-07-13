from app.platform_core.release_candidate.readiness import InternalRCReadinessGate

def test_readiness(): assert InternalRCReadinessGate().run()['ready'] is True
