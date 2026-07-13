from app.platform_core.desktop_launcher.build_readiness import DesktopInternalBuildReadiness

def test_build_readiness(): assert DesktopInternalBuildReadiness().readiness()['internal_desktop_build_ready'] is True
