from app.v500_alpha50_packaging_enablement.models import GuardedPackagingEnablementSummaryV500Alpha50

def test_summary():
 s=GuardedPackagingEnablementSummaryV500Alpha50(); assert s.ready and s.test_pack_size==90 and s.build_id=='2026.50.C.001'
