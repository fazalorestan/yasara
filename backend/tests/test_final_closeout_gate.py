from app.final_closeout_v1.closeout_gate import CloseoutGateBuilderV1

def test_closeout_gate():
    gate = CloseoutGateBuilderV1().build()
    assert gate.passed is True
