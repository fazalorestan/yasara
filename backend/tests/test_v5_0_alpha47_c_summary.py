from app.v500_alpha47_artifact_release.models import ArtifactReleaseSummaryV500Alpha47

def test_summary():
 s=ArtifactReleaseSummaryV500Alpha47(); assert s.ready and s.test_pack_size==90 and s.build_id=='2026.47.C.001'
