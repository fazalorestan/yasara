from app.decision_v1.domain.models import DecisionDirection
from app.execution_v1.domain.models import ExecutionIntent, ExecutionMode, ExecutionSide
from app.execution_v1.engine.safety_gate import ExecutionSafetyGateV1

def test_safety_gate_rejects_invalid_quantity():
    intent = ExecutionIntent(symbol="BTC/USDT", direction=DecisionDirection.LONG, side=ExecutionSide.BUY, quantity=0)
    result = ExecutionSafetyGateV1().validate(intent)
    assert result.passed is False

def test_safety_gate_accepts_dry_run():
    intent = ExecutionIntent(symbol="BTC/USDT", direction=DecisionDirection.LONG, side=ExecutionSide.BUY, quantity=0.01, mode=ExecutionMode.DRY_RUN)
    result = ExecutionSafetyGateV1().validate(intent)
    assert result.passed is True
