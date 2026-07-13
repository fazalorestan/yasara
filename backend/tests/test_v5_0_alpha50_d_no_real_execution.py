from app.v500_alpha50_artifact_registration.service import LocalExeArtifactRegistrationFacadeV500Alpha50

def test_no_real_execution(): assert LocalExeArtifactRegistrationFacadeV500Alpha50().report()['real_execution_enabled'] is False
