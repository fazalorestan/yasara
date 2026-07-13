from app.platform_core.windows_builder.portable_build_contract import WindowsPortableBuildContract

def test_portable():
 assert WindowsPortableBuildContract().contract()['portable_build_supported'] is True
