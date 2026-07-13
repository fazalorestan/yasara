from app.v52_alpha_native_launcher.models import NativeWindowsLauncherSummaryV52Alpha

def test_summary():
 s=NativeWindowsLauncherSummaryV52Alpha(); assert s.ready and s.test_pack_size==90 and s.build_id=='2026.52.D.001'
