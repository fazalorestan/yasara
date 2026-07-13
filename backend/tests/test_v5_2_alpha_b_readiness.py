from app.platform_core.first_real_exe_build.readiness import FirstRealExeBuildReadinessGate

def test_readiness(): assert FirstRealExeBuildReadinessGate().run()['ready'] is True
