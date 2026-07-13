from app.v500_alpha49_windows_portable_build.models import WindowsPortableBuildSummaryV500Alpha49

def test_summary():
 s=WindowsPortableBuildSummaryV500Alpha49(); assert s.ready and s.test_pack_size==90 and s.build_id=='2026.49.D.001'
