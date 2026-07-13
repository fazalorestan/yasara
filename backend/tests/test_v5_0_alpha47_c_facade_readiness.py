from app.v500_alpha47_artifact_release.service import ArtifactReleaseFacadeV500Alpha47

def test_facade_readiness():
 r=ArtifactReleaseFacadeV500Alpha47().readiness(); assert r is not None
