from app.platform_core.windows_real_exe.spec_contract import WindowsExeSpecContract

def test_spec(): assert WindowsExeSpecContract().spec()['requires_runtime_bootstrap'] if False else WindowsExeSpecContract().spec()['ready'] is True
