from app.platform_core.windows_packaging_enablement.pyinstaller_check import PyInstallerAvailabilityCheck

def test_pyinstaller(): assert PyInstallerAvailabilityCheck().check()['must_be_available_before_execute'] is True
