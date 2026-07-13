from app.platform_core.windows_real_exe.readiness import WindowsRealExeBuildPipelineReadinessGate

def test_readiness(): assert WindowsRealExeBuildPipelineReadinessGate().run()['ready'] is True
