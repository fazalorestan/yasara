from app.platform_core.release_registry.readiness import ArtifactReleaseReadinessGate

def test_readiness(): assert ArtifactReleaseReadinessGate().run()['ready'] is True
