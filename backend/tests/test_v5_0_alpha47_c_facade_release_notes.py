from app.v500_alpha47_artifact_release.service import ArtifactReleaseFacadeV500Alpha47

def test_facade_release_notes():
 r=ArtifactReleaseFacadeV500Alpha47().release_notes(); assert r is not None
