from app.v425_policy_gate.gate import PluginPolicyGateV425
from app.v425_policy_gate.models import PolicyContextV425, PolicyRequirementV425

def test_v425_policy_gate_blocked():
    ctx = PolicyContextV425()
    req = PolicyRequirementV425(permission="p", license="pro", feature_flag="f", require_authentication=True)
    result = PluginPolicyGateV425().evaluate(ctx, req)
    assert result["allowed"] is False
    assert result["live_execution_enabled"] is False
