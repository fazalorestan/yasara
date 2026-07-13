from app.production_packaging_v1.rollback_manager import RollbackManagerV1

def test_rollback_manager_plan():
    plan = RollbackManagerV1().plan("1.0.0")
    assert "restore_backup" in plan.actions
