from app.v425_policy_gate.execution_contract import ExecutionIsolationGuardV425

def test_v425_execution_contract():
    c = ExecutionIsolationGuardV425().execution_contract()
    assert c["ready"] is True
    assert c["live_execution_enabled"] is False
