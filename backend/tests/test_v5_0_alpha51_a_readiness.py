from app.platform_core.windows_exe_smoke_build.readiness import WindowsExeSmokeBuildReadinessGate

def test_readiness(): assert WindowsExeSmokeBuildReadinessGate().run()['ready'] is True
