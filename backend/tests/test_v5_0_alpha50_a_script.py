from app.platform_core.windows_real_exe.build_script import WindowsRealExeBuildScriptContract

def test_script(): assert WindowsRealExeBuildScriptContract().contract()['real_execution_enabled'] is False
