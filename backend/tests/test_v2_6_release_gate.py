from app.v26_final_operational.service import FinalOperationalBridgeServiceV26

def test_v26_release_gate():
    g = FinalOperationalBridgeServiceV26().release_gate()
    assert g["ready"] is True
    assert g["gate"] == "PASSED"
    assert g["remaining_to_full_operational_percent"] == 0
