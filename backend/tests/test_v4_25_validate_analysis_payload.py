from app.v425_policy_gate.execution_contract import ExecutionIsolationGuardV425

def test_v425_validate_analysis_payload():
    guard = ExecutionIsolationGuardV425()
    ok = guard.validate_analysis_payload({"signal": "wait"})
    bad = guard.validate_analysis_payload({"execute_order": True})
    assert ok["valid"] is True
    assert bad["valid"] is False
