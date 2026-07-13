from app.rc1_v1.rollback_validation import RollbackValidationPlannerV1

def test_rc1_rollback_validation():
    plan = RollbackValidationPlannerV1().build()
    assert "restore_backup" in plan.checks
