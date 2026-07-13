from app.platform_core.cryptography_runtime_dependency_fix.readiness import CryptographyRuntimeDependencyFixReadinessGate

def test_readiness(): assert CryptographyRuntimeDependencyFixReadinessGate().run()['ready'] is True
