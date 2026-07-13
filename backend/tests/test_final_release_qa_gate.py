from app.final_release_v1.final_qa_gate import FinalQAGateBuilderV1

def test_final_qa_gate():
    gate = FinalQAGateBuilderV1().build()
    assert gate.passed is True
