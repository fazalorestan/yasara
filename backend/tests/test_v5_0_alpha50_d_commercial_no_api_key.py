from app.v500_alpha50_artifact_registration.service import LocalExeArtifactRegistrationFacadeV500Alpha50

def test_commercial_no_api_key(): assert LocalExeArtifactRegistrationFacadeV500Alpha50().report()['commercial_api_key_required'] is False
