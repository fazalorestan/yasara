from app.v500_alpha46_desktop_host.models import DesktopHostSummaryV500Alpha46

def test_summary():
 s=DesktopHostSummaryV500Alpha46(); assert s.ready and s.test_pack_size==80 and s.exe_packaging_enabled is False
