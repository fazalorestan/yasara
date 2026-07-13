from app.v500_alpha47_artifact_release.service import ArtifactReleaseFacadeV500Alpha47

def test_commercial_no_api_key(): assert ArtifactReleaseFacadeV500Alpha47().report()['commercial_api_key_required'] is False
