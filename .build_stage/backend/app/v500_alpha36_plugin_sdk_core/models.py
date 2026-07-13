from pydantic import BaseModel

class PluginSDKCoreSummaryV500Alpha36(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_36_enterprise_plugin_sdk_package_a"
    scope: str = "plugin_sdk_core_manifest_registry"
    plugin_manifest: bool = True
    plugin_registry: bool = True
    loader_contract: bool = True
    compatibility_check: bool = True
    safety_contract: bool = True
    real_execution_enabled: bool = False
    auto_trading_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 60
