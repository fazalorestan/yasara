from app.platform_core.plugin_sdk.sandbox import PluginSandboxPolicy

def test_v500_alpha36_b_sandbox_ok(): assert PluginSandboxPolicy().evaluate({'capabilities':['analytics']})['allowed'] is True