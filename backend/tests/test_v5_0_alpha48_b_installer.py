from app.platform_core.windows_packaging.installer_contract import WindowsInstallerContract

def test_installer(): assert WindowsInstallerContract().contract()['ready'] is True
