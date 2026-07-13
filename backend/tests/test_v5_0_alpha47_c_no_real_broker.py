from app.v500_alpha47_artifact_release.service import ArtifactReleaseFacadeV500Alpha47

def test_no_real_broker(): assert ArtifactReleaseFacadeV500Alpha47().report()['real_broker_connection_enabled'] is False
