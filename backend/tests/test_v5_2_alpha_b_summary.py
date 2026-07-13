from app.v52_alpha_first_real_exe_build.models import FirstRealExeBuildSummaryV52Alpha

def test_summary():
 s=FirstRealExeBuildSummaryV52Alpha(); assert s.ready and s.test_pack_size==90 and s.build_id=='2026.52.B.001'
