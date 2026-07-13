from app.v500_alpha51_exe_smoke_build.models import WindowsExeSmokeBuildSummaryV500Alpha51

def test_summary():
 s=WindowsExeSmokeBuildSummaryV500Alpha51(); assert s.ready and s.test_pack_size==90 and s.build_id=='2026.51.A.001'
