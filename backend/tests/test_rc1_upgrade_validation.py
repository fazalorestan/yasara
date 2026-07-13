from app.rc1_v1.upgrade_validation import UpgradeValidationPlannerV1

def test_rc1_upgrade_validation():
    plan = UpgradeValidationPlannerV1().build()
    assert "backup_created" in plan.checks
