from app.v500_alpha50_artifact_registration.models import LocalExeArtifactRegistrationSummaryV500Alpha50

def test_summary():
 s=LocalExeArtifactRegistrationSummaryV500Alpha50(); assert s.ready and s.test_pack_size==90 and s.build_id=='2026.50.D.001'
