from app.platform_core.operations.recovery import RecoveryChecklist

def test_v433_recovery():
    c = RecoveryChecklist().checklist()
    assert c["ready"] is True
    assert "live_execution_disabled" in c["items"]
