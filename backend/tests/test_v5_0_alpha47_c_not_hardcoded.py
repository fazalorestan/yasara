from app.v500_alpha47_artifact_release.service import ArtifactReleaseFacadeV500Alpha47

def test_not_hardcoded(): assert ArtifactReleaseFacadeV500Alpha47().report()['hardcoded_dashboard'] is False
