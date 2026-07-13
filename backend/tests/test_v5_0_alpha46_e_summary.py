from app.v500_alpha46_desktop_foundation.models import DesktopFoundationSummaryV500Alpha46

def test_summary():
 s=DesktopFoundationSummaryV500Alpha46(); assert s.ready and s.test_pack_size==85 and s.exe_packaging_enabled is False
