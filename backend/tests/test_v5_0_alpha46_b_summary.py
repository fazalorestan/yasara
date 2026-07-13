from app.v500_alpha46_desktop_ui.models import DesktopUISummaryV500Alpha46

def test_summary():
 s=DesktopUISummaryV500Alpha46(); assert s.ready and s.test_pack_size==80 and s.hardcoded_dashboard is False
