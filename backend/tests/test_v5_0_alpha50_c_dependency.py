from app.platform_core.windows_packaging_enablement.dependency_check import LocalPackagingDependencyCheck

def test_dependency(): assert LocalPackagingDependencyCheck().check()['pyinstaller_required'] is True
