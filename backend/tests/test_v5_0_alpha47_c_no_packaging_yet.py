from app.v500_alpha47_artifact_release.service import ArtifactReleaseFacadeV500Alpha47

def test_no_packaging_yet(): assert ArtifactReleaseFacadeV500Alpha47().summary().packaging_enabled is False
