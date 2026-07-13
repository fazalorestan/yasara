from pydantic import BaseModel
class PluginRuntimeSandboxSummaryV500Alpha36(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_36_enterprise_plugin_sdk_package_b"
    scope: str = "plugin_runtime_sandbox"
    plugin_runtime: bool = True
    sandbox_policy: bool = True
    permission_gate: bool = True
    lifecycle_hooks: bool = True
    plugin_health: bool = True
    real_execution_enabled: bool = False
    auto_trading_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 60
