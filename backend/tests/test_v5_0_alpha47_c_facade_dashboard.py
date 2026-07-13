from app.v500_alpha47_artifact_release.service import ArtifactReleaseFacadeV500Alpha47

def test_facade_dashboard():
 r=ArtifactReleaseFacadeV500Alpha47().dashboard(); assert r is not None
