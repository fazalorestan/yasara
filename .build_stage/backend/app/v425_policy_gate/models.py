from pydantic import BaseModel, Field

class PolicyGateSummaryV425(BaseModel):
    ready: bool = True
    phase: str = "v4_25_plugin_policy_gate_execution_contract"
    scope: str = "architecture_evolution"
    mode: str = "report_only"
    no_new_trading_features: bool = True
    live_execution_enabled: bool = False
    backward_compatible: bool = True
    constitution_compliant: bool = True
    safety: str = "policy_infrastructure_only_no_real_execution"

class PolicyContextV425(BaseModel):
    authenticated: bool = False
    role: str = "guest"
    permissions: list[str] = Field(default_factory=list)
    licenses: list[str] = Field(default_factory=list)
    entitlements: list[str] = Field(default_factory=list)
    feature_flags: dict[str, bool] = Field(default_factory=dict)
    risk_approved: bool = False
    environment: str = "local"

class PolicyRequirementV425(BaseModel):
    permission: str | None = None
    license: str | None = None
    entitlement: str | None = None
    feature_flag: str | None = None
    require_risk_approval: bool = False
    require_authentication: bool = False
