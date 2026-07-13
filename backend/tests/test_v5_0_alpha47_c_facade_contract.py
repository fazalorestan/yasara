from app.v500_alpha47_artifact_release.service import ArtifactReleaseFacadeV500Alpha47

def test_facade_contract():
 r=ArtifactReleaseFacadeV500Alpha47().contract(); assert r is not None
