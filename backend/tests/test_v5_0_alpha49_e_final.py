from app.platform_core.desktop_finalization.final_report import InternalDesktopBuildFinalReport

def test_final(): assert InternalDesktopBuildFinalReport().report()['desktop_host_ready'] is True
