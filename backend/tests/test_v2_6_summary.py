from app.v26_final_operational.service import FinalOperationalBridgeServiceV26

def test_v26_summary():
    s = FinalOperationalBridgeServiceV26().summary()
    assert s.operational_progress_percent == 100
    assert s.remaining_to_full_operational_percent == 0
