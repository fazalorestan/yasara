from app.platform_core.windows_builder.exe_build_contract import WindowsExeBuildContract

def test_exe():
 assert WindowsExeBuildContract().contract()['requires_manifest'] is True
