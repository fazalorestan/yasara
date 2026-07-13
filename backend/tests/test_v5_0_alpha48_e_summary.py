from app.v500_alpha48_windows_builder.models import WindowsExecutableBuilderSummaryV500Alpha48

def test_summary():
 s=WindowsExecutableBuilderSummaryV500Alpha48(); assert s.ready and s.test_pack_size==90 and s.build_id=='2026.48.E.001'
