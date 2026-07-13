from pydantic import BaseModel, Field

class PluginCatalogSummaryV423(BaseModel):
    ready: bool = True
    phase: str = "v4_23_plugin_manifest_catalog_governance_bridge"
    scope: str = "architecture_evolution"
    no_new_trading_features: bool = True
    backward_compatible: bool = True
    safety: str = "infrastructure_only_no_real_execution"
    constitution_compliant: bool = True

class PluginManifestV423(BaseModel):
    name: str
    version: str
    category: str = "business_plugin"
    metadata: dict = Field(default_factory=dict)
    dependencies: list[str] = Field(default_factory=list)
    feature_flags: list[str] = Field(default_factory=list)
    required_permissions: list[str] = Field(default_factory=list)
    required_licenses: list[str] = Field(default_factory=list)
    event_registration: list[str] = Field(default_factory=list)
    routes: list[str] = Field(default_factory=list)
    services: list[str] = Field(default_factory=list)
    tests: list[str] = Field(default_factory=list)
    documentation: list[str] = Field(default_factory=list)
