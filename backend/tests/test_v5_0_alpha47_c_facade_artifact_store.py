from app.v500_alpha47_artifact_release.service import ArtifactReleaseFacadeV500Alpha47

def test_facade_artifact_store():
 r=ArtifactReleaseFacadeV500Alpha47().artifact_store(); assert r is not None
