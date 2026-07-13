from app.platform_core.windows_exe_build.readiness import WindowsExeBuildScriptReadinessGate

def test_readiness(): assert WindowsExeBuildScriptReadinessGate().run()['ready'] is True
