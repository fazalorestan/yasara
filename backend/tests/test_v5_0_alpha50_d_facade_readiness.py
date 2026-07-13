from app.v500_alpha50_artifact_registration.service import LocalExeArtifactRegistrationFacadeV500Alpha50

def test_facade_readiness(): assert LocalExeArtifactRegistrationFacadeV500Alpha50().readiness() is not None
