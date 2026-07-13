from app.v500_alpha49_desktop_launcher.models import DesktopRuntimeLauncherSummaryV500Alpha49

def test_summary():
 s=DesktopRuntimeLauncherSummaryV500Alpha49(); assert s.ready and s.test_pack_size==90 and s.build_id=='2026.49.C.001'
