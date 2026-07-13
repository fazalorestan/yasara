from app.platform_core.windows_builder.installer_build_contract import WindowsInstallerBuildContract

def test_installer():
 assert WindowsInstallerBuildContract().contract()['installer_build_supported'] is True
