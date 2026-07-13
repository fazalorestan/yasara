from app.rc1_hardening_v1.rc_validation_summary import RCHardeningSummaryBuilderV1

def test_rc_hardening_summary():
    summary = RCHardeningSummaryBuilderV1().build()
    assert summary.ready is True
    assert summary.next_step == "final_release_candidate"
