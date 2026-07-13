from app.platform_core.windows_artifact_registration.readiness import LocalExeArtifactRegistrationReadinessGate

def test_readiness(): assert LocalExeArtifactRegistrationReadinessGate().run()['ready'] is True
