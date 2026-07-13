from app.v425_policy_gate.gate import PluginPolicyGateV425
from app.v425_policy_gate.models import PolicyContextV425, PolicyRequirementV425

def test_v425_policy_gate_allowed():
    ctx = PolicyContextV425(authenticated=True, role="admin", permissions=["p"], licenses=["pro"], entitlements=["e"], feature_flags={"f": True}, risk_approved=True)
    req = PolicyRequirementV425(permission="p", license="pro", entitlement="e", feature_flag="f", require_risk_approval=True, require_authentication=True)
    result = PluginPolicyGateV425().evaluate(ctx, req)
    assert result["allowed"] is True
    assert result["execution_allowed"] is False
