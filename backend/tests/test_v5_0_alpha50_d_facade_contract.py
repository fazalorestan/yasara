from app.v500_alpha50_artifact_registration.service import LocalExeArtifactRegistrationFacadeV500Alpha50

def test_facade_contract(): assert LocalExeArtifactRegistrationFacadeV500Alpha50().contract() is not None
