from app.v500_alpha47_artifact_release.service import ArtifactReleaseFacadeV500Alpha47

def test_commercial_no_execution(): assert ArtifactReleaseFacadeV500Alpha47().report()['commercial_execution_engine_enabled'] is False
