from app.v500_alpha48_windows_packaging.models import WindowsPackagingSummaryV500Alpha48

def test_summary():
 s=WindowsPackagingSummaryV500Alpha48(); assert s.ready and s.test_pack_size==90 and s.build_id=='2026.48.B.001'
