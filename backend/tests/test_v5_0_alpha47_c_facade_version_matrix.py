from app.v500_alpha47_artifact_release.service import ArtifactReleaseFacadeV500Alpha47

def test_facade_version_matrix():
 r=ArtifactReleaseFacadeV500Alpha47().version_matrix(); assert r is not None
