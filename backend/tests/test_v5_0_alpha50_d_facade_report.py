from app.v500_alpha50_artifact_registration.service import LocalExeArtifactRegistrationFacadeV500Alpha50

def test_facade_report(): assert LocalExeArtifactRegistrationFacadeV500Alpha50().report() is not None
