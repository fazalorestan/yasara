from app.v500_alpha48_windows_app.models import WindowsAppBootstrapSummaryV500Alpha48

def test_summary():
 s=WindowsAppBootstrapSummaryV500Alpha48(); assert s.ready and s.test_pack_size==90 and s.build_id=='2026.48.A.001'
