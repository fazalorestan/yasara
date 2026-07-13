from app.v500_alpha47_artifact_release.service import ArtifactReleaseFacadeV500Alpha47

def test_facade_build_history():
 r=ArtifactReleaseFacadeV500Alpha47().build_history(); assert r is not None
