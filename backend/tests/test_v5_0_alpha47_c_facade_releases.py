from app.v500_alpha47_artifact_release.service import ArtifactReleaseFacadeV500Alpha47

def test_facade_releases():
 r=ArtifactReleaseFacadeV500Alpha47().releases(); assert r is not None
