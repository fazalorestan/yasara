from pydantic import BaseModel
class PluginVersioningSummaryV500Alpha36(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_36_enterprise_plugin_sdk_package_c"
    scope: str = "plugin_versioning_compatibility"
    version_manager: bool = True
    compatibility_matrix: bool = True
    dependency_contract: bool = True
    upgrade_planner: bool = True
    marketplace_metadata: bool = True
    real_execution_enabled: bool = False
    auto_trading_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 60
