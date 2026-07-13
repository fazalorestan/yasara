from app.platform_core.windows_portable_build.build_script_contract import WindowsPortableBuildScriptContract

def test_script(): assert WindowsPortableBuildScriptContract().contract()['does_not_enable_real_execution'] is True
