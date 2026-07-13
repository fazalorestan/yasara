from app.v500_alpha50_artifact_registration.service import LocalExeArtifactRegistrationFacadeV500Alpha50

def test_no_real_broker(): assert LocalExeArtifactRegistrationFacadeV500Alpha50().report()['real_broker_connection_enabled'] is False
