from app.v500_alpha49_native_desktop.models import NativeDesktopApplicationSummaryV500Alpha49

def test_summary():
 s=NativeDesktopApplicationSummaryV500Alpha49(); assert s.ready and s.test_pack_size == 90 and s.build_id == '2026.49.A.001'
