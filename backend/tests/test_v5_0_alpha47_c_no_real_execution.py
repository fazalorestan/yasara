from app.v500_alpha47_artifact_release.service import ArtifactReleaseFacadeV500Alpha47

def test_no_real_execution(): assert ArtifactReleaseFacadeV500Alpha47().report()['real_execution_enabled'] is False
