from app.v500_alpha50_windows_real_exe.models import WindowsRealExeBuildPipelineSummaryV500Alpha50

def test_summary():
 s=WindowsRealExeBuildPipelineSummaryV500Alpha50(); assert s.ready and s.test_pack_size==90 and s.build_id=='2026.50.A.001'
