from app.v500_alpha50_windows_exe_build.models import WindowsExeBuildScriptSummaryV500Alpha50

def test_summary():
 s=WindowsExeBuildScriptSummaryV500Alpha50(); assert s.ready and s.test_pack_size==90 and s.build_id=='2026.50.B.001'
